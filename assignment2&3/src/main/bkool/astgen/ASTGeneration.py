from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
#from main.bkool.utils.AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program(self.visit(ctx.classDecls()))

    def visitClassDecls(self, ctx:BKOOLParser.ClassDeclsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.getChild(0))] + self.visit(ctx.classDecls())
        else:
            return [self.visit(ctx.getChild(0))]
    

    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        if ctx.getChildCount() == 4:
            return ClassDecl(Id(ctx.ID(0).getText()), [], None)
        elif ctx.getChildCount() == 5:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memberListNoNull()), None)
        elif ctx.getChildCount() == 6 and ctx.EXTENDS():
            return ClassDecl(Id(ctx.ID(0).getText()), [], Id(ctx.ID(1).getText()))
        else:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memberListNoNull()), Id(ctx.ID(1).getText()))

            

    def visitMemberListNoNull(self, ctx:BKOOLParser.MemberListNoNullContext):
        num = ctx.getChildCount()
        lis = []
        for i in range(num):
            obj = self.visit(ctx.getChild(i))
            if isinstance(obj, list):
                for k in obj:
                    lis.append(k)
            else:
                lis.append(obj)
        return lis

    def visitClassAttr(self, ctx:BKOOLParser.ClassAttrContext):
        typ = self.visit(ctx.typ())
        attrDecls = self.visit(ctx.attrDecls())
        kind = None
        if ctx.STATIC():
            kind = Static()
        else:
            kind = Instance()
        if ctx.FINAL():
            return [AttributeDecl(kind, ConstDecl(a[0],typ,a[1])) for a in attrDecls]
        else:
            return [AttributeDecl(kind, VarDecl(a[0],typ,a[1])) for a in attrDecls]
            


    def visitAttrDecls(self, ctx:BKOOLParser.AttrDeclsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.attrDecl())
        else:
            return self.visit(ctx.attrDecl()) + self.visit(ctx.attrDecls())

    def visitAttrDecl(self, ctx:BKOOLParser.AttrDeclContext):
        if ctx.getChildCount() == 1:
            return [(Id(ctx.ID().getText()), None)]
        else:
            return [(Id(ctx.ID().getText()), self.visit(ctx.expr()))]


    def visitClassMethod(self, ctx:BKOOLParser.ClassMethodContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.constructor())
        elif ctx.getChildCount() == 5:
            kind = Instance()
            typ = self.visit(ctx.methodtype())
            if ctx.ID().getText() == 'main' and isinstance(typ, VoidType):
                kind = Static()
            return MethodDecl(kind, Id(ctx.ID().getText()), [], typ, self.visit(ctx.blockStmt()))
        elif ctx.getChildCount() == 6 and ctx.STATIC():
            return MethodDecl(Static(), Id(ctx.ID().getText()), [], self.visit(ctx.methodtype()), self.visit(ctx.blockStmt()))
        elif ctx.getChildCount() == 6 and ctx.params():
            return MethodDecl(Instance(), Id(ctx.ID().getText()), self.visit(ctx.params()), self.visit(ctx.methodtype()), self.visit(ctx.blockStmt()))
        else:
            return MethodDecl(Static(), Id(ctx.ID().getText()), self.visit(ctx.params()), self.visit(ctx.methodtype()), self.visit(ctx.blockStmt()))
            
            
            


    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        if ctx.getChildCount() == 4:
            return MethodDecl(Instance(), Id('<init>'), [], None, self.visit(ctx.blockStmt()))
        else:
            return MethodDecl(Instance(), Id('<init>'), self.visit(ctx.params()), None, self.visit(ctx.blockStmt()))


    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        else:
            return self.visit(ctx.param()) + self.visit(ctx.params())

    def visitParam(self, ctx:BKOOLParser.ParamContext):
        ids = self.visit(ctx.ids())
        list = []
        for id in ids:
            list.append(VarDecl(id, self.visit(ctx.typ()), None))
        return list

    def visitIds(self, ctx:BKOOLParser.IdsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())

    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):
        if ctx.getChildCount() == 2:
            return Block([],[])
        elif ctx.getChildCount() == 4:
            return Block(self.visit(ctx.varDecls()), self.visit(ctx.stmts()))
        elif ctx.getChildCount() == 3 and ctx.varDecls():
            return Block(self.visit(ctx.varDecls()), [])
        else:
            return Block([], self.visit(ctx.stmts()))

    def visitVarDecls(self, ctx:BKOOLParser.VarDeclsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.varDecl())
        else:
            return self.visit(ctx.varDecl()) + self.visit(ctx.varDecls())


    def visitVarDecl(self, ctx:BKOOLParser.VarDeclContext):
        listvar = self.visit(ctx.listVar())     #a=1, b, c=2, d
        list = []
        if ctx.FINAL():
            for ele in listvar:
                list.append(ConstDecl(ele[0], self.visit(ctx.typ()), ele[1]))
        else:
            for ele in listvar:
                list.append(VarDecl(ele[0], self.visit(ctx.typ()), ele[1]))
        return list

    def visitListVar(self, ctx:BKOOLParser.ListVarContext):
        if ctx.COMMA() and ctx.getChildCount() == 3:
            return [(Id(ctx.ID().getText()),None)] + self.visit(ctx.listVar())
        elif ctx.COMMA() and ctx.getChildCount() > 3:
            return [(Id(ctx.ID().getText()), self.visit(ctx.expr()))] + self.visit(ctx.listVar())
        elif ctx.getChildCount() == 1:
            return [(Id(ctx.ID().getText()), None)]
        else:
            return [(Id(ctx.ID().getText()), self.visit(ctx.expr()))]

        

    #OK BELOW
    def visitStmts(self, ctx:BKOOLParser.StmtsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        else:
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmts())

    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visit(ctx.getChild(0))

    def visitAssignStmt(self, ctx:BKOOLParser.AssignStmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.expr8())

    #OK BELOW
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        if ctx.getChildCount() == 4:
            return If(self.visit(ctx.expr()), self.visit(ctx.getChild(3)))
        else:
            return If(self.visit(ctx.expr()), self.visit(ctx.getChild(3)), self.visit(ctx.getChild(5)))


    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.getChild(3)), self.visit(ctx.getChild(5)), ctx.getChild(4).getText() == 'to', self.visit(ctx.stmt()))

    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        return Break()

    def visitContiStmt(self, ctx:BKOOLParser.ContiStmtContext):
        return Continue()

    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return Return(self.visit(ctx.expr()))


    def visitInvoStmt(self, ctx:BKOOLParser.InvoStmtContext):
        if ctx.getChildCount() == 6:
            return CallStmt(self.visit(ctx.expr9()), Id(ctx.ID().getText()), [])
        else:
            return CallStmt(self.visit(ctx.expr9()), Id(ctx.ID().getText()), self.visit(ctx.exprs()))


    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))


    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.getChildCount() == 3:
            return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))


    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        elif ctx.getChildCount() == 2:
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr6()))

    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr7()))
        

    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.getChild(0)), self.visit(ctx.expr())) 

    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.getChild(0)), Id(ctx.getChild(2).getText()))
        elif ctx.getChildCount() == 5:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.getChild(2).getText()), [])
        elif ctx.getChildCount() == 6:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.getChild(2).getText()), self.visit(ctx.exprs()))
            

    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr11())
        elif ctx.getChildCount() == 5:
            return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.exprs()))
        elif ctx.getChildCount() == 4:
            return NewExpr(Id(ctx.ID().getText()), [])
            

    
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLIT():
            val = True
            if ctx.BOOLIT().getText() == 'true':
                val = True
            elif ctx.BOOLIT().getText() == 'false':
                val = False 
            return BooleanLiteral(val)
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.sube():
            return self.visit(ctx.sube())
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        


    def visitSube(self, ctx:BKOOLParser.SubeContext):
        return self.visit(ctx.expr())



    def visitExprs(self, ctx:BKOOLParser.ExprsContext):
        # Return list of expression
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprs())

    def visitArraytype(self, ctx: BKOOLParser.ArraytypeContext):
        size = int(ctx.INTLIT().getText())
        if ctx.INTTYPE():
            return ArrayType(size, IntType())
        elif ctx.FLOATTYPE():
            return ArrayType(size, FloatType())
        elif ctx.STRING():
            return ArrayType(size, StringType())
        elif ctx.BOOLEAN():
            return ArrayType(size, BoolType())
        elif ctx.ID():
            return ArrayType(size, ClassType(Id(ctx.ID().getText())))


    
    def visitPtype(self, ctx:BKOOLParser.PtypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())              #Array type
        

    def visitTyp(self, ctx:BKOOLParser.TypContext):
        if ctx.ptype():
            return self.visit(ctx.ptype())
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))

    def visitMethodtype(self, ctx:BKOOLParser.MethodtypeContext):
        # Return method type: ptype or void
        if ctx.typ():
            return self.visit(ctx.typ())
        else:
            return VoidType()


    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.ele_list()))


    def visitEle(self, ctx:BKOOLParser.EleContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLIT():
            val = True
            if ctx.BOOLIT().getText() == 'true':
                val = True
            elif ctx.BOOLIT().getText() == 'false':
                val = False 
            return BooleanLiteral(val)
        

    def visitEle_list(self, ctx:BKOOLParser.Ele_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.ele())]
        else:
            return [self.visit(ctx.ele())] + self.visit(ctx.ele_list())