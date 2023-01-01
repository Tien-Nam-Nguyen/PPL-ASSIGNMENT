
"""
 * @author nhphung
"""

from AST import * 
from Visitor import *
#from Utils import Utils
from StaticError import *
#from main.bkool.utils.AST import *
import copy

class ClasType:
    def __init__(self, name, this=False, nul=False):
        self.name = name
        self.this = this
        self.nul = nul
    
    def __eq__(self, other):
        return self.name == other.name

class VarBox:
    def __init__(self, name, const, typ):
        '''
            name: string
            const: True if const
            typ: loai
        '''
        self.name = name
        self.const = const
        self.typ = typ
    
    def __eq__(self, other):
        return self.name == other.name


class AttriBox:
    def __init__(self, name, static, const, typ):
        '''
            name: string 
            static: True if static
            const: True if const 
        '''
        self.name = name
        self.static = static
        self.const = const
        self.typ = typ
    
    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return 'AttriBox'


class MethodBox:
    def __init__(self, name, static, params, block, typ):
        '''
            name: string
            static: True if static
            params: list of VarBox
            block: list of list of decl
            typ: type
        '''
        self.name = name
        self.static = static
        self.params = params
        self.block = block
        self.typ = typ
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __str__(self):
        return 'MethodBox'
    
    

class ClassBox:
    def __init__(self, name, mems, parent):
        '''
            name: string
            mems: list of attribute or method
            parent: string
        '''
        self.name = name
        self.mems = mems
        self.parent = parent
    
    def __eq__(self, other):
        return self.name == other.name




class GetEnv(BaseVisitor):
    
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
        ClassBox('io', [
            MethodBox('readInt', True, [], None,IntType()),
            MethodBox('writeInt', True, [VarBox('anArg', False, IntType())], None,VoidType()),
            MethodBox('writeIntLn', True, [VarBox('anArg', False, IntType())], None,VoidType()),
            MethodBox('readFloat', True, [], None, FloatType()),
            MethodBox('writeFloat', True, [VarBox('anArg', False, FloatType())], None, VoidType()),
            MethodBox('writeFloatLn', True, [VarBox('anArg', False, FloatType())], None,VoidType()),
            MethodBox('readBool', True, [], None, BoolType()),
            MethodBox('writeBool', True, [VarBox('anArg', False, BoolType())], None, VoidType()),
            MethodBox('writeBoolLn', True, [VarBox('anArg', False, BoolType())], None,VoidType()),
            MethodBox('readStr', True, [], None, StringType()),
            MethodBox('writeStr', True, [VarBox('anArg', False, StringType())], None, VoidType()),
            MethodBox('writeStrLn', True, [VarBox('anArg', False, StringType())], None, VoidType())
        ], None)
    ]
    
    def check(self):
        return self.visit(self.ast, self.global_envi)
    
    def visitProgram(self, ast, param):
        for class_decl in ast.decl:
            self.visit(class_decl, param)
        
        
        return param
        
    def visitClassDecl(self, ast, param):
        classname = self.visit(ast.classname, ['getid'])
        this_class = ClassBox(classname, None, None)
        if this_class in param:
            raise Redeclared(Class(), classname)

        env = []
        for mem in ast.memlist:
            self.visit(mem, env)
        
        this_class.mems = env
        if ast.parentname:
            this_class.parent = self.visit(ast.parentname, ['getid'])

        param.append(this_class)
    

    def visitAttributeDecl(self, ast, param):           #param: list of attri or method
        this_attri = AttriBox(None, isinstance(self.visit(ast.kind, param), Static), None, None)
        store = self.visit(ast.decl, {'attri': []})             #vardecl or constdecl
        this_attri.name, this_attri.const, this_attri.typ = store.name, store.const, store.typ 

        if this_attri in param:
            raise Redeclared(Attribute(), this_attri.name)
        
        param.append(this_attri)


    def visitMethodDecl(self, ast, param):              #param: list of attri or method
        methodname = self.visit(ast.name, ['getid'])
        this_method = MethodBox(methodname, isinstance(self.visit(ast.kind, param), Static), None, None, None)
        if ast.returnType:
            this_method.typ = self.visit(ast.returnType, param)
            
        

        if this_method in param:
            raise Redeclared(Method(), methodname)
        
        
        
        env = {'param': []}
        for pa in ast.param:        #pa is vardecl
            self.visit(pa, env)
        
        this_method.params = env['param']
        
        
        block_env = copy.deepcopy(env)  #env.copy()
        #block_env['var'] = [[]]             #block_env: {'param': [...],  'var': [[]]}
        
        self.visit(ast.body, block_env)
        #this_method.block = block_env['var']   

        param.append(this_method)
        

    def visitVarDecl(self, ast, param):
        varname = self.visit(ast.variable, ['getid'])
        this_var = VarBox(varname, False, self.visit(ast.varType, param))
        if len(param) == 1 and 'attri' in param:
            return this_var
        
        if 'param' in param and len(param) == 1:
            if this_var in param['param']:
                raise Redeclared(Parameter(), varname)
            param['param'].append(this_var)
        
        elif 'var' in param and len(param) == 1:                #Block ngoai cung(than ham)
            if this_var in param['var'][0]:
                raise Redeclared(Variable(), varname)
            param['var'][0].append(this_var)


    
    def visitConstDecl(self, ast, param):
        constname = self.visit(ast.constant, ['getid'])
        this_const = VarBox(constname, True, self.visit(ast.constType, param))
        if len(param) == 1 and 'attri' in param:
            return this_const
         
        if 'var' in param and len(param) == 1:
            if this_const in param['var'][0]:
                raise Redeclared(Constant(), constname)
            param['var'][0].append(this_const)
    
    
    def visitStatic(self, ast, param):
        return Static()
    
    def visitInstance(self, ast, param):
        return Instance()
    
    def visitIntType(self, ast, param):
        return IntType()
    
    def visitFloatType(self, ast, param):
        return FloatType()
    
    def visitBoolType(self, ast, param):
        return BoolType()
    
    def visitStringType(self, ast, param):
        return StringType()
    
    def visitVoidType(self, ast, param):
        return VoidType()
    
    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, self.visit(ast.eleType, param))
    
    def visitClassType(self, ast, param):
        return ClasType(self.visit(ast.classname, ['getid']))
    
    def visitBlock(self, ast, param):           #param: already have param, block_env {'param': [...]}
        env = {}
        if 'param' in param and len(param) == 1:
            env['var'] = [param['param']]                              
        elif 'var' in param and len(param) == 1:
            env['var'] = [[]] + param['var']              #param: {'var': [[], [...]]}
        
        for decl in ast.decl:
            self.visit(decl, env)             #visit vardecl or constdecl

        #env: {'var': [[...]]}             or  env{'var': [[..], [..]]}
        for st in ast.stmt:                     
            self.visit(st, env)
        
        #param: {'var': [[...]]} and inner_block: {'var': [[...], [...]]}

        
    
    def visitId(self, ast, param):                                      
        this_id = VarBox(ast.name, None, None)
        if isinstance(param, list) and param[0] == 'getid':             #param: getid 
            return ast.name
        
        '''
        if 'var' in param:
            for scope in param['var']:                                             #param: list of list(scope)
                if this_id in scope:
                    return
            raise Undeclared(Identifier(), ast.name)'''

    
    def visitIf(self, ast, param):          #param: {'var': [[...]]}
        self.visit(ast.expr, param)
        self.visit(ast.thenStmt, param)
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
    
    def visitFor(self, ast, param):
        self.visit(ast.id, param)
        self.visit(ast.expr1, param)
        self.visit(ast.expr2, param)
        #self.visit(ast.up, param)
        self.visit(ast.loop, param)
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        self.visit(ast.expr, param)
    
    def visitAssign(self, ast, param):              #param: {'var': [[...]]}
        self.visit(ast.lhs, param)                 #lhs: id or arr[2] or this.a or this.a[2]
        self.visit(ast.exp, param)
    
    def visitCallStmt(self, ast, param):
        self.visit(ast.obj, param)
        #self.visit(ast.method, param)
        for pa in ast.param:                    #pa: expr
            self.visit(pa, param)

    def visitArrayCell(self, ast, param):           #param: {'var': [[...], [...]]}
        self.visit(ast.arr, param)
        self.visit(ast.idx, param)
    
    def visitFieldAccess(self, ast, param):
        self.visit(ast.obj, param)
        #self.visit(ast.fieldname, param)
    
    def visitBinaryOp(self, ast, param):
        self.visit(ast.left, param)
        self.visit(ast.right, param)
    
    def visitUnaryOp(self, ast, param):
        self.visit(ast.body, param)
    
    def visitCallExpr(self, ast, param):
        self.visit(ast.obj, param)
        for pa in ast.param:
            self.visit(pa, param)
    
    def visitNewExpr(self, ast, param):
        #self.visit(ast.classname, param)
        for pa in ast.param:
            self.visit(pa, param)
    
    def visitIntLiteral(self, ast, param):
        return None
    
    def visitFloatLiteral(self, ast, param):
        return None
    
    def visitBooleanLiteral(self, ast, param):
        return None
    
    def visitStringLiteral(self, ast, param):
        return None
    
    def visitNullLiteral(self, ast, param):
        return None
    
    def visitSelfLiteral(self, ast, param):
        return None 
    
    def visitArrayLiteral(self, ast, param):
        return None

class StaticChecker(BaseVisitor):

    global_envi = []
            
    
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
        

    def visitProgram(self,ast, c): 
        StaticChecker.global_envi = GetEnv(self.ast).check()
        for x in ast.decl:
            self.visit(x, c)
        return []
        #return [self.visit(x,c) for x in ast.decl]

    
    def visitClassDecl(self, ast, param):       #param: list of classdecl
        classname = self.visit(ast.classname, ['getid'])
        classhold = self.getClassBox(classname)

        for mem in ast.memlist:
            self.visit(mem, ('class',classhold))              #classhold:  (classname, ClassBox)
        
        if ast.parentname:
            parentname = self.visit(ast.parentname, ['getid'])
            self.getClassBox(parentname)

        
    

    def visitAttributeDecl(self, ast, param):           #param: ('class', ClassBox)
        self.visit(ast.kind, ('attri', param[1]))
        self.visit(ast.decl, ('attri', param[1]))


    def visitMethodDecl(self, ast, param):              #param: ('class', ClassBox)
        method_name = self.visit(ast.name, ['getid'])
        
        self.visit(ast.body, (f'method{method_name}', param[1]))                # ('method', ClassBox)
        #this_method.block = block_env['var']   

        

    def visitVarDecl(self, ast, param):             #param: ('attri', ClassBox)       OR ('block', ClassBox, [[...]], MethodBox)
        name = self.visit(ast.variable, ['getid'])
        vartyp = self.visit(ast.varType, param)
        this_var = VarBox(name, False, vartyp)
        if param[0] == 'attri':                     #visit from Attri
            if ast.varInit:
                typ,_ = self.visit(ast.varInit, ('attri', param[1], [['out']], None))
                self.checkConstantType(vartyp, typ, ast, False)

        elif param[0] in ['block', 'forblock']:               #visit from block
            param[2][0].append(this_var)
            if ast.varInit:
                typ,_ = self.visit(ast.varInit, ('var', param[1], param[2], param[3]))
                self.checkConstantType(vartyp, typ, ast, False)


    
    def visitConstDecl(self, ast, param):          #param: ('attri', ClassBox)       OR ('block', ClassBox, [[..]], MethodBox)
        name = self.visit(ast.constant, ['getid'])
        constyp = self.visit(ast.constType, param)
        this_const = VarBox(name, True, constyp)
        if param[0] == 'attri':    
            if ast.value:                  #visit from Attri
                typ, cons = self.visit(ast.value, ('attri', param[1], [['out']], None))
                if not cons:
                    raise IllegalConstantExpression(ast.value)
                self.checkConstantType(constyp, typ, ast, True)
            else:
                raise IllegalConstantExpression(ast.value)  

        elif param[0] in ['block', 'forblock']:               #visit from block
            param[2][0].append(this_const)
            if ast.value:
                typ, cons = self.visit(ast.value, ('const', param[1], param[2], param[3]))
                if not cons:
                    raise IllegalConstantExpression(ast.value)
                self.checkConstantType(constyp, typ, ast, True)
            else:
                raise IllegalConstantExpression(ast.value)

    
    
    def visitStatic(self, ast, param):
        return Static()
    
    def visitInstance(self, ast, param):
        return Instance()
    
    def visitIntType(self, ast, param):
        return IntType()
    
    def visitFloatType(self, ast, param):
        return FloatType()
    
    def visitBoolType(self, ast, param):
        return BoolType()
    
    def visitStringType(self, ast, param):
        return StringType()
    
    def visitVoidType(self, ast, param):
        return VoidType()
    
    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, self.visit(ast.eleType, param))
    
    def visitClassType(self, ast, param):
        name = self.visit(ast.classname, ['getid'])
        box = self.getClassBox(name)
        return ClasType(box.name)
    
    def visitBlock(self, ast, param):           #param: ('method{}', ClassBox) or param: ('block', ClassBox, [[]], MethodBox)
        env = []
        ancient = 'block'

        if len(param) == 4:
            method = param[3]

        if param[0][0:6] == 'method':                 #visit from a method
            env = [[]] + env
            method = self.getMethod(param[0][6:], param[1])
            for pa in method.params:
                env[0].append(pa)                          
        elif param[0] == 'block':                       #visit from block
            env = [[]] + param[2]                       #env: [[], [...]]
        elif param[0] == 'for' or param[0] == 'forblock':
            env = [[]] + param[2]
            ancient = 'forblock'
        elif param[0] == 'if':
            env = [[]] + param[2]
    
        
        for decl in ast.decl:
            self.visit(decl, (ancient, param[1], env, method))             #visit vardecl or constdecl

        #env: [[...]]     param:  ('method', ClassBox)
        for st in ast.stmt:                     
            self.visit(st, (ancient, param[1], env, method))
        
        #param: {'var': [[...]]} and inner_block: {'var': [[...], [...]]}

        
    
    def visitId(self, ast, param):                      #param: ('..', ClassBox, [[...]], MethodBox)             or         ('...', ClassBox)    
        this_id = VarBox(ast.name, None, None)
        if isinstance(param, list) and param[0] == 'getid':             #param: getid 
            return ast.name
        
        if param[0] in ['field', 'calle', 'calls']:                 #visit from field   ('field', ..., '...')
            att = True if param[0] == 'field' else False
            if len(param[2][0]) != 0 and isinstance(param[2][0][0],str) and param[2][0][0] == 'this':               #this class's attribute access  ('field', ClassBox, [['this']], MethodBox)
                mem = self.getMem(this_id.name, param[1], att)
                 
                if not mem.static:
                    return mem
                #raise IllegalMemberAccess(ast)
                return 'illegal member access'

            elif len(param[2][0]) != 0 and isinstance(param[2][0][0],str) and param[2][0][0] == 'out' :        #static field ('field', ClassBox, [['out']], MethodBox) no block obj luot di
                return (self.getClassBox(this_id.name), None)

            elif len(param[2][0]) != 0 and isinstance(param[2][0][0],str) and param[2][0][0] == 'stamem':    #luot ve cua static field chung  ('field', ClassBox(obj), [['stamem']], MethodBox)
                mem = self.getMem(this_id.name, param[1], att)
                if mem.static:
                    return mem
                #raise IllegalMemberAccess(ast)
                return 'illegal member access'
            
            elif len(param[2][0]) != 0 and isinstance(param[2][0][0],str) and param[2][0][0] == 'idmem':        #luot ve cua id in block ('field', ClassBox(obj), [['idmem']], MethodBox)
                mem = self.getMem(this_id.name, param[1], att)
                if not mem.static:
                    return mem
                #raise IllegalMemberAccess(ast)
                return 'illegal member access'

            else:# len(param[2][0]) != 0 and param[2][0][0] not in ['out', 'stamem', 'this', 'idmem']:                #('field', CLassBox, [[...]], MethodBox) in block luot di
                hold = self.findInScope(this_id.name, param[2])
                if hold is not None:
                    return (hold.typ, None)
                else:
                    return (self.getClassBox(this_id.name), None)

            
        else:                                                           #visit from everywhere as variable/id
            if len(param[2][0]) != 0 and isinstance(param[2][0][0], str) and param[2][0][0] == 'out':             #param:  ('...', ClassBox, [['out']], MethodBox)
                raise Undeclared(Identifier(), this_id.name)
            else:           #param:  ('...', ClassBox, [[...]], MethodBox)
                id = self.findInScope(this_id.name, param[2])
                '''
                if param[0] == 'assignl':
                    if id != None:
                        if id.const:
                            return 'cannot assign to constant'      '''
                if id is not None:
                    return (id.typ, id.const)
                raise Undeclared(Identifier(), this_id.name)


         
        

    
    def visitIf(self, ast, param):          #param: ('', ClassBox, [[...]], MethodBox)
        typ,_ = self.visit(ast.expr, ('if', param[1], param[2], param[3]))

        if not isinstance(typ, BoolType):
            raise TypeMismatchInStatement(ast)

        label = 'if'

        if param[0] == 'forblock':
            label = 'forblock' 

        self.visit(ast.thenStmt, (label, param[1], param[2], param[3]))
        if ast.elseStmt:
            self.visit(ast.elseStmt, (label, param[1], param[2], param[3]))
    
    def visitFor(self, ast, param):
        idtyp,consornot = self.visit(ast.id, ('forblock', param[1], param[2], param[3]))

        if consornot:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))

        expr1,_ = self.visit(ast.expr1, ('forblock', param[1], param[2], param[3]))
        expr2,_ = self.visit(ast.expr2, ('forblock', param[1], param[2], param[3]))

        if not isinstance(idtyp, IntType) or not isinstance(expr1, IntType) or not isinstance(expr2, IntType):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.loop, ('forblock', param[1], param[2], param[3]))        #sua ngay 13/12
    
    def visitContinue(self, ast, param):
        if param[0] != 'forblock':
            raise MustInLoop(ast)
    
    def visitBreak(self, ast, param):
        if param[0] != 'forblock':
            raise MustInLoop(ast)
    
    def visitReturn(self, ast, param):
        if param[3] is not None and isinstance(param[3], MethodBox):
            returntype = param[3].typ
        
        typ,_ = self.visit(ast.expr, ('return', param[1], param[2], param[3]))

        #if returntype == None and param[3].name == '<init>':
        #    raise TypeMismatchInStatement(ast)              #Moi them ngay 7/12

        if type(returntype) != type(typ):
            if isinstance(returntype, FloatType) and isinstance(typ, IntType):
                return 
            if isinstance(returntype, VoidType) and isinstance(typ,ClasType) and typ.nul:
                return
            raise TypeMismatchInStatement(ast)

        #type(lhs[0]) == type(rhs[0])
        if isinstance(returntype,ClasType):
            if returntype.name == typ.name or self.haveParent(typ.name, returntype.name):
                return
            raise TypeMismatchInStatement(ast)
        
        if isinstance(returntype, ArrayType):
            if returntype.size == typ.size and (type(returntype.eleType) == type(typ.eleType) or (isinstance(returntype.eleType,FloatType) and isinstance(typ.eleType,IntType))):
                return 
            raise TypeMismatchInStatement(ast)


    
    def visitAssign(self, ast, param):              #param: ('...', ClassBox, [[...]], MethodBox)
        lhs = self.visit(ast.lhs, ('assignl',param[1], param[2], param[3]))                 #lhs: (typ, boolean)
        if lhs[1]:          #lhs is constant
            raise CannotAssignToConstant(ast)
        rhs = self.visit(ast.exp, ('assignr', param[1], param[2], param[3])) #rhs: (typ, boolean)


        if type(lhs[0]) != type(rhs[0]):
            if isinstance(lhs[0], FloatType) and isinstance(rhs[0], IntType):
                return 
            raise TypeMismatchInStatement(ast)

        #type(lhs[0]) == type(rhs[0])
        if isinstance(lhs[0],ClasType):
            if lhs[0].name == rhs[0].name or rhs[0].nul or self.haveParent(rhs[0].name, lhs[0].name):
                return
            raise TypeMismatchInStatement(ast)
        
        if isinstance(lhs[0], ArrayType):
            if lhs[0].size == rhs[0].size and (type(lhs[0].eleType) == type(rhs[0].eleType) or (isinstance(lhs[0].eleType,FloatType) and isinstance(rhs[0].eleType,IntType))):
                return 
            raise TypeMismatchInStatement(ast)
        



    
    def visitCallStmt(self, ast, param):                    #param: ('...', ClassBox, [[...]], MethodBox)
        obj = self.visit(ast.obj, ('calls', param[1], param[2], param[3]))        #(typ,boolean)
        if isinstance(obj[0], ClasType) and obj[0].this:
            mem = self.visit(ast.method, ('calls', param[1], [['this']], param[3]))
        elif isinstance(obj[0], ClassBox):
            mem = self.visit(ast.method, ('calls', obj[0], [['stamem']], param[3]))
        elif isinstance(obj[0], ClasType):
            clas = self.getClassBox(obj[0].name)
            mem = self.visit(ast.method, ('calls', clas, [['idmem']], param[3]))
        else:
            raise TypeMismatchInStatement(ast)

        if isinstance(mem, str) and mem == 'illegal member access':
            raise IllegalMemberAccess(ast)
            
        if not isinstance(mem.typ, VoidType) or len(ast.param) != len(mem.params):
            raise TypeMismatchInStatement(ast)

        for pa1, pa2 in zip(ast.param, mem.params):
            arg,_ = self.visit(pa1, ('call', param[1], param[2], param[3]))              #pa1: expr    

            #analyze arg and pa2.typ
            if type(arg) != type(pa2.typ):
                if isinstance(pa2.typ, FloatType) and isinstance(arg, IntType):
                    pass 
                else:
                    raise TypeMismatchInStatement(ast)

            if isinstance(arg, ClasType):
                if arg.name == pa2.typ.name or self.haveParent(arg.name, pa2.typ.name):
                    pass
                else:
                    raise TypeMismatchInStatement(ast)
            
            if isinstance(arg, ArrayType):
                if arg.size == pa2.typ.size and (type(arg.eleType) == type(pa2.typ.eleType) or (isinstance(arg.eleType, IntType) and isinstance(pa2.typ.eleType, FloatType))):
                    pass
                else: 
                    raise TypeMismatchInStatement(ast)


    def visitArrayCell(self, ast, param):           #param: {'...',ClassBox,[[...]], MethodBox}
        arr = self.visit(ast.arr, ('cell', param[1], param[2], param[3]))             #(typ, boolean)
        if not isinstance(arr[0], ArrayType):
            raise TypeMismatchInExpression(ast)
        
        idx = self.visit(ast.idx,('cell', param[1], param[2], param[3]))
        if not isinstance(idx[0],IntType):
            raise TypeMismatchInExpression(ast)
        
        return (arr[0].eleType, arr[1])
    

    def visitFieldAccess(self, ast, param):         #param: ('..', ClassBox, [['out']],MethodBox) or ('...', ClassBox, [[...]], MethodBox) 
        obj = self.visit(ast.obj, ('field', param[1], param[2], param[3]))  #(typ, boolean)
        if isinstance(obj[0], ClasType) and obj[0].this:
            mem = self.visit(ast.fieldname, ('field', param[1], [['this']], param[3]))        #('field', ClassBox, [['this']])
            if isinstance(mem, str) and mem == 'illegal member access':
                raise IllegalMemberAccess(ast)
            return (mem.typ, mem.const)
            
        elif isinstance(obj[0], ClassBox):               #another object
            mem = self.visit(ast.fieldname, ('field', obj[0], [['stamem']], param[3]))       #('field', ClassBox(obj), [['stamem']])
            if isinstance(mem, str) and mem == 'illegal member access':
                raise IllegalMemberAccess(ast)
            return (mem.typ, mem.const)

        elif isinstance(obj[0], ClasType):
            clas = self.getClassBox(obj[0].name)
            mem = self.visit(ast.fieldname, ('field', clas, [['idmem']], param[3]))         #('field', ClassBox(obj), [['idmem']])
            if isinstance(mem, str) and mem == 'illegal member access':
                raise IllegalMemberAccess(ast)
            return (mem.typ, mem.const)
        else:
            raise TypeMismatchInExpression(ast)
            
    
    def visitBinaryOp(self, ast, param):            #('...', ClassBox, [['out']], MethodBox)  or  ('...', ClassBox, [[...]], MethodBox)
        
        left = self.visit(ast.left, ('binop', param[1], param[2], param[3]))
        right = self.visit(ast.right, ('binop', param[1], param[2], param[3]))    #(typ, boolean)

        if isinstance(left[0], VoidType) or isinstance(right[0], VoidType):
            raise TypeMismatchInExpression(ast)

        kin = left[1] and right[1]

        if type(left[0]) in [IntType, FloatType] and type(right[0]) in [IntType, FloatType]:      #operand have int type or float type
            if ast.op in ['+', '-', '*']:
                if type(left[0]) == type(right[0]):                    
                    return (left[0], kin)
                elif type(left[0]) != type(right[0]):
                    return (FloatType(), kin)
            elif ast.op in ['\\', '%']:
                if type(left[0]) == type(right[0]) == IntType:
                    return (IntType(), kin)
                raise TypeMismatchInExpression(ast)
            elif ast.op == '/':
                return (FloatType(), kin)
            elif ast.op in ['==', '!=']:
                if type(left[0]) == type(right[0]) == IntType:
                    return (BoolType(), kin)
                raise TypeMismatchInExpression(ast)
            elif ast.op in ['<', '<=', '>', '>=']:
                return (BoolType(), kin)
            
        elif type(left[0]) == type(right[0]) == BoolType:
            if ast.op in ['&&', '||']:
                return (BoolType(), kin)
            elif ast.op in ['==', '!=']:
                return (BoolType(), kin)
        elif type(left[0]) == type(right[0]) == StringType:
            if ast.op == '^':
                return (StringType(), kin)
        
        raise TypeMismatchInExpression(ast)
        

    
    def visitUnaryOp(self, ast, param):             #param: ('...', ClassBox, [[...]], MethodBox)
        
        body = self.visit(ast.body, ('unaop', param[1], param[2], param[3]))

        if isinstance(body[0], VoidType):
            raise TypeMismatchInExpression(ast)

        if type(body[0]) in [IntType, FloatType]:
            if ast.op in ['+', '-']:
                return (body[0], body[1]) 
        elif type(body[0]) == BoolType:
            if ast.op == '!':
                return (BoolType(), body[1])
        
        raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast, param):        #param: ('...', ClassBox, [['out']], MethodBox) or ('...', ClassBox, [[..]], MethodBox)
        obj = self.visit(ast.obj, ('calle', param[1], param[2], param[3]))
        mem = None
        if isinstance(obj[0], ClasType) and obj[0].this:
            mem = self.visit(ast.method, ('calle', param[1], [['this']], param[3]))
        elif isinstance(obj[0], ClassBox):
            mem = self.visit(ast.method, ('calle', obj[0], [['stamem']], param[3]))
        elif isinstance(obj[0], ClasType):
            clas = self.getClassBox(obj[0].name)
            mem = self.visit(ast.method, ('calle', clas, [['idmem']], param[3]))
        else:
            raise TypeMismatchInExpression(ast)
        
        if isinstance(mem, str) and mem == 'illegal member access':
            raise IllegalMemberAccess(ast)

        if isinstance(mem.typ, VoidType) or len(ast.param) != len(mem.params):
            raise TypeMismatchInExpression(ast)

        for pa1, pa2 in zip(ast.param, mem.params):
            arg,_ = self.visit(pa1, ('call', param[1], param[2], param[3]))              #pa1: expr    


            #analyze arg and pa2.typ
            if type(arg) != type(pa2.typ):
                if isinstance(pa2.typ, FloatType) and isinstance(arg, IntType):
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
                

            if isinstance(arg, ClasType):
                if arg.name == pa2.typ.name or self.haveParent(arg.name, pa2.typ.name):
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            
            if isinstance(arg, ArrayType):
                if arg.size == pa2.typ.size and (type(arg.eleType) == type(pa2.typ.eleType) or (isinstance(arg.eleType, IntType) and isinstance(pa2.typ.eleType, FloatType))):
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
        
        return (mem.typ, False)
    
    def visitNewExpr(self, ast, param):
        classname = self.visit(ast.classname, ['getid'])
        classbox = self.getClassBox(classname)
        
        init = self.getMem('<init>', classbox, False, spec= True)       #chuaco hoac la mot member
        if len(ast.param) == 0 and (isinstance(init, str) or (not isinstance(init, str) and len(init.params) == 0)):
            return (ClasType(classname), False)

        init = self.getMem('<init>', classbox, False)       #MethodBox
        if len(init.params) != len(ast.param):
            raise TypeMismatchInExpression(ast)
        
        for pa1, pa2 in zip(ast.param, init.params):
            arg,_ = self.visit(pa1, ('new', param[1], param[2], param[3]))              #pa1: expr    

            #analyze arg and pa2.typ
            if type(arg) != type(pa2.typ):
                if isinstance(pa2.typ, FloatType) and isinstance(arg, IntType):
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
                

            if isinstance(arg, ClasType):
                if arg.name == pa2.typ.name or self.haveParent(arg.name, pa2.typ.name):
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            
            if isinstance(arg, ArrayType):
                if arg.size == pa2.typ.size and (type(arg.eleType) == type(pa2.typ.eleType) or (isinstance(arg.eleType, IntType) and isinstance(pa2.typ.eleType, FloatType))):
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
            
        return (ClasType(classname), False)
    
    def visitIntLiteral(self, ast, param):
        return (IntType(), True)
    
    def visitFloatLiteral(self, ast, param):
        return (FloatType(), True)
    
    def visitBooleanLiteral(self, ast, param):
        return (BoolType(), True)
    
    def visitStringLiteral(self, ast, param):
        return (StringType(), True)
    
    def visitNullLiteral(self, ast, param):
        return (ClasType('', False, True), True)
    
    def visitSelfLiteral(self, ast, param):
        name = param[1].name
        return (ClasType(name, True), True)
    
    def visitArrayLiteral(self, ast, param):
        first = True
        eletype = None
        for ele in ast.value:
            eletyp, cons = self.visit(ele, param)
            if first:
                eletype = eletyp
                first = False
            if type(eletyp) not in [IntType,FloatType,BoolType,StringType] or type(eletyp) != type(eletype):
                    raise IllegalArrayLiteral(ast)
            
        return (ArrayType(len(ast.value), eletype), True)

    def getClassBox(self, name):
        for clas in StaticChecker.global_envi:
            if clas.name == name:
                return clas
        raise Undeclared(Class(), name)

    def getMethod(self, name, classbox):
        for mem in classbox.mems:
            if name == mem.name:
                return mem
        raise Undeclared(Method(), name)

    def getMem(self, name, classbox, att, spec=False):              #mem: True if mem is attribute
        if att:
            kieu = 'AttriBox'
        else:
            kieu = 'MethodBox'

        while True:
            for mem in classbox.mems:
                if name == mem.name and kieu == str(mem):
                    return mem
            if classbox.parent is not None:
                classbox = self.getClassBox(classbox.parent)
            else:
                if spec:
                    return 'chuaco'
                if att:
                    raise Undeclared(Attribute(), name)
                else:
                    raise Undeclared(Method(), name)

    def findInScope(self, name, listOfScope):        
        for scope in listOfScope:
            for ele in scope:
                if name == ele.name:
                    return ele
        
        return None

    def haveParent(self, name, parentname):
        classbox = self.getClassBox(name)
        if classbox.parent is not None:
            while True:
                if classbox.parent == parentname:
                    return True
                classbox = self.getClassBox(classbox.parent)
                if classbox.parent is None:
                    return False
        else:
            return False

    def checkConstantType(self, constyp, typ, ast, isconstant):
        if type(constyp) != type(typ):
            if isinstance(constyp, FloatType) and isinstance(typ, IntType):
                return
            if isconstant: 
                raise TypeMismatchInConstant(ast)
            raise TypeMismatchInStatement(ast)

        #type(lhs[0]) == type(rhs[0])
        if isinstance(constyp,ClasType):
            if constyp.name == typ.name or typ.nul or self.haveParent(typ.name, constyp.name):
                return
            if isconstant:
                raise TypeMismatchInConstant(ast)
            raise TypeMismatchInStatement(ast)

        if isinstance(constyp, ArrayType):
            if constyp.size == typ.size and (type(constyp.eleType) == type(typ.eleType) or (isinstance(constyp.eleType,FloatType) and isinstance(typ.eleType,IntType))):
                return 
            if isconstant:
                raise TypeMismatchInConstant(ast)
            raise TypeMismatchInStatement(ast)


'''
    class A{
	int x = 1;
	float y = this.x;
	final string z = "str";
	static boolean t;
	void foo(){
		int x;
		int i;
		if x > 2 then{
			for i:=1 to 10 do{
				x := x + 2;			
			} 
		}
	}
}
'''