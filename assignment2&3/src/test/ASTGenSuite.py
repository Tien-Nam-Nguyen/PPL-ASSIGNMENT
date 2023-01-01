import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_1(self):
        """Simple program: class main {} """
        input = """class main {
                    int a;
                }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_2(self):
        """Simple program: class main {} """
        input = """class main {
                    int a, b, c, d;
                }"""
        expect = str(Program([ClassDecl(Id('main'),[AttributeDecl(Instance(),VarDecl(Id('a'),IntType())),AttributeDecl(Instance(),VarDecl(Id('b'),IntType())),AttributeDecl(Instance(),VarDecl(Id('c'),IntType())),AttributeDecl(Instance(),VarDecl(Id("d"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_3(self):
        """Simple program: class main {} """
        input = """class main {
                    int a = 1;
                }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id('a'),IntType(),IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_4(self):
        """Simple program: class main {} """
        input = """class main {
                    int a, b=12, c, d=2;
                }"""
        expect = str(Program([ClassDecl(Id('main'),[AttributeDecl(Instance(),VarDecl(Id('a'),IntType())),AttributeDecl(Instance(),VarDecl(Id('b'),IntType(),IntLiteral(12))),AttributeDecl(Instance(),VarDecl(Id('c'),IntType())),AttributeDecl(Instance(),VarDecl(Id('d'),IntType(),IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test_5(self):
        """Simple program: class main {} """
        input = """class main {
                    int a;
                    float b = 12.2;
                    string c = "stringc";
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("b"),FloatType(),FloatLiteral(12.2))),AttributeDecl(Instance(),VarDecl(Id("c"),StringType(),StringLiteral("\"stringc\"")))])])
        )
        self.assertTrue(TestAST.test(input,expect,305))
    
    def test_6(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    final static int a;
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),None))])])
        )
        self.assertTrue(TestAST.test(input,expect,306))
    
    def test_7(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    main(){}
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test_8(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    main(){}
                    int getB(){

                    }
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),MethodDecl(Instance(),Id("getB"),[],IntType(),Block([],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,308))

    def test_9(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    main(){}
                    static int getB(){

                    }
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),MethodDecl(Static(),Id("getB"),[],IntType(),Block([],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,309))
    
    def test_10(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    main(){}
                    static boolean getB(int c){

                    }
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),MethodDecl(Static(),Id("getB"),[VarDecl(Id("c"),IntType())],BoolType(),Block([],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,310))
    
    def test_11(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    main(){}
                    static boolean getB(int c; string str1,str2){}
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[])),MethodDecl(Static(),Id("getB"),[VarDecl(Id("c"),IntType()),VarDecl(Id("str1"),StringType()),VarDecl(Id("str2"),StringType())],BoolType(),Block([],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,311))

    def test_12(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    static int smain(){}
                    static boolean getB(int c; string str1,str2){}
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Static(),Id("smain"),[],IntType(),Block([],[])),MethodDecl(Static(),Id("getB"),[VarDecl(Id("c"),IntType()),VarDecl(Id("str1"),StringType()),VarDecl(Id("str2"),StringType())],BoolType(),Block([],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,312))

    def test_13(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    #This is a comment
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2)))])])
        )
        self.assertTrue(TestAST.test(input,expect,313))

    def test_14(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    string a = "#This is a comment";
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),StringLiteral("\"#This is a comment\"")))])])
        )
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test_15(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    string a = "#This is a comment";
                    int[12] a;
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),StringLiteral("\"#This is a comment\""))),AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(12,IntType())))])])
        )
        self.assertTrue(TestAST.test(input,expect,315))

    def test_16(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    string a = "#This is a comment";
                    int[12] a;
                    string[12] c;
                    float[0] d;
                    boolean[1202001230] e;
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),StringLiteral("\"#This is a comment\""))),AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(12,IntType()))),AttributeDecl(Instance(),VarDecl(Id("c"),ArrayType(12,StringType()))),AttributeDecl(Instance(),VarDecl(Id("d"),ArrayType(0,FloatType()))),AttributeDecl(Instance(),VarDecl(Id("e"),ArrayType(1202001230,BoolType())))])])
        )
        self.assertTrue(TestAST.test(input,expect,316))
    def test_17(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    string a = "#This is a comment";
                    main(){
                        int[12] a;
                    string[12] c;
                        float[0] d;
                    boolean[1202001230] e;
                    }
                    
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),StringLiteral("\"#This is a comment\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([VarDecl(Id("a"),ArrayType(12,IntType())),VarDecl(Id("c"),ArrayType(12,StringType())),VarDecl(Id("d"),ArrayType(0,FloatType())),VarDecl(Id("e"),ArrayType(1202001230,BoolType()))],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,317))

    def test_18(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    string a = "#This is a comment";
                    main(){
                        final int[12] a = 12;
                    }
                    
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),StringLiteral("\"#This is a comment\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("a"),ArrayType(12,IntType()),IntLiteral(12))],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,318))
    
    def test_19(self):
        """Simple program: class main {} """
        input = """class main extends parent{
                    static float b = 1.2;
                    string a = "#This is a comment";
                    main(){
                        final int[12] a = 12;
                    }
                    
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),StringLiteral("\"#This is a comment\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("a"),ArrayType(12,IntType()),IntLiteral(12))],[]))],Id("parent"))])
        )
        self.assertTrue(TestAST.test(input,expect,319))

    def test_20(self):
        """Simple program: class main {} """
        input = """class main extends parent{
                    static float b = 1.2;
                    main(){
                        final int[12] a = 12;
                        float c = 12.2 + 100%3;
                    }
                    
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("a"),ArrayType(12,IntType()),IntLiteral(12)),VarDecl(Id("c"),FloatType(),BinaryOp("+",FloatLiteral(12.2),BinaryOp("%",IntLiteral(100),IntLiteral(3))))],[]))],Id("parent"))])
        )
        self.assertTrue(TestAST.test(input,expect,320))
    
    def test_21(self):
        """Simple program: class main {} """
        input = """class main extends parent{
                    static float b = 1.2;
                    maini(int a,b;float d){
                        final int[12] a = 12;
                        float c = 12.2 + 100%3;
                    }
                    
                    
                }"""
        expect = str(
            Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("d"),FloatType())],None,Block([ConstDecl(Id("a"),ArrayType(12,IntType()),IntLiteral(12)),VarDecl(Id("c"),FloatType(),BinaryOp("+",FloatLiteral(12.2),BinaryOp("%",IntLiteral(100),IntLiteral(3))))],[]))],Id("parent"))])
        )
        self.assertTrue(TestAST.test(input,expect,321))

    def test_22(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    static void maini(int a;float d){
                        final int[12] a = {1,2,3,4};
                    }
                    
                    
                }"""
        expect = str(
Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Static(),Id("maini"),[VarDecl(Id("a"),IntType()),VarDecl(Id("d"),FloatType())],VoidType(),Block([ConstDecl(Id("a"),ArrayType(12,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))],[]))])])
        )
        self.assertTrue(TestAST.test(input,expect,322))

    def test_23(self):
        """Simple program: class main {} """
        input = """class main {
                    static float b = 1.2;
                    int foo(){
                        int a = 12;
                        a := b + 1;
                        {}
                    }
                    
                    
                }"""
        expect = str(
Program([ClassDecl(Id("main"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("a"),IntType(),IntLiteral(12))],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(1))),Block([],[])]))])])
        )
        self.assertTrue(TestAST.test(input,expect,323))
    
    def test_24(self):
        """Simple program: class main {} """
        input = """class Ex {
                    static float b = 1.2;
                    int foo(){
                        boolean[1] arr = {true};
                        arr[0] := false;
                        return arr;
                    } 
                    
                }"""
        expect = str(
Program([ClassDecl(Id("Ex"),[AttributeDecl(Static(),VarDecl(Id("b"),FloatType(),FloatLiteral(1.2))),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("arr"),ArrayType(1,BoolType()),ArrayLiteral([BooleanLiteral(True)]))],[Assign(ArrayCell(Id("arr"),IntLiteral(0)),BooleanLiteral(False)),Return(Id("arr"))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test_25(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    int foo(){
                        boolean[1] arr = {true};
                        arr[0] := false;
                        arr[2] := nil;
                        arr[3] := this.a;
                        return this.a;
                    } 
                    
                }"""
        expect = str(
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("arr"),ArrayType(1,BoolType()),ArrayLiteral([BooleanLiteral(True)]))],[Assign(ArrayCell(Id("arr"),IntLiteral(0)),BooleanLiteral(False)),Assign(ArrayCell(Id("arr"),IntLiteral(2)),NullLiteral()),Assign(ArrayCell(Id("arr"),IntLiteral(3)),FieldAccess(SelfLiteral(),Id("a"))),Return(FieldAccess(SelfLiteral(),Id("a")))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,325))

    def test_26(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    int foo(){
                        float b = 12e4;
                        if true then this.a := b;
                    } 
                    
                }"""
        expect = str(
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("b"),FloatType(),FloatLiteral(120000.0))],[If(BooleanLiteral(True),Assign(FieldAccess(SelfLiteral(),Id("a")),Id("b")))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test_27(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    int foo(){
                        float b = 12e4;
                        if true then this.a := b; else this.a := c;
                    } 
                    
                }"""
        expect = str(
    Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("b"),FloatType(),FloatLiteral(120000.0))],[If(BooleanLiteral(True),Assign(FieldAccess(SelfLiteral(),Id("a")),Id("b")),Assign(FieldAccess(SelfLiteral(),Id("a")),Id("c")))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,327))
    
    def test_28(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    int foo(){
                        final float b = 12e4;
                        if true then this.a := b; else this.a := c;
                        b := a[2];
                    } 
                    
                }"""
        expect = str(
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([ConstDecl(Id("b"),FloatType(),FloatLiteral(120000.0))],[If(BooleanLiteral(True),Assign(FieldAccess(SelfLiteral(),Id("a")),Id("b")),Assign(FieldAccess(SelfLiteral(),Id("a")),Id("c"))),Assign(Id("b"),ArrayCell(Id("a"),IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,328))
    
    def test_29(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    int foo(){
                        if (d >= 2) then{
                            d := d + 1;
                            if d > 5 then return 5;
                        }
                        else{
                            d := (d - 1) * 2;
                        }
                    }    
                }"""
        expect = str(
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp(">=",Id("d"),IntLiteral(2)),Block([],[Assign(Id("d"),BinaryOp("+",Id("d"),IntLiteral(1))),If(BinaryOp(">",Id("d"),IntLiteral(5)),Return(IntLiteral(5)))]),Block([],[Assign(Id("d"),BinaryOp("*",BinaryOp("-",Id("d"),IntLiteral(1)),IntLiteral(2)))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,329))
    
    def test_30(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    int foo(){
                        if (d >= 2) then{
                            d := d + 1;
                            if d > 5 then return 5;
                        }
                        else{
                            d := d - 1 * 2 + 3 / 2 + a[23];
                        }
                    }    
                }"""
        expect = str(                                                                                                                                                                                                                                                                                                                                                                                                                                               #d := d - 1 * 2 + 3 / 2 + a[23];                                        
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp(">=",Id("d"),IntLiteral(2)),Block([],[Assign(Id("d"),BinaryOp("+",Id("d"),IntLiteral(1))),If(BinaryOp(">",Id("d"),IntLiteral(5)),Return(IntLiteral(5)))]),Block([],[Assign(Id("d"),BinaryOp("+",BinaryOp("+",BinaryOp("-",Id("d"),BinaryOp("*",IntLiteral(1),IntLiteral(2))),BinaryOp("/",IntLiteral(3),IntLiteral(2))),ArrayCell(Id("a"),IntLiteral(23))))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,330)) 
    
    def test_31(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(){
                        return nil;
                    }
                    int foo(){
                        if (d >= 2) then{
                            d := d + 1;
                            if d > 5 then return 5;
                        }
                        else{
                            d := a + this.func() * 1.2;

                        }
                    }    
                }"""
        expect = str(                                                                                                                                                                                                                                                                                                                                                                                                                                               #d := d - 1 * 2 + 3 / 2 + a[23];                                        
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[],FloatType(),Block([],[Return(NullLiteral())])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp(">=",Id("d"),IntLiteral(2)),Block([],[Assign(Id("d"),BinaryOp("+",Id("d"),IntLiteral(1))),If(BinaryOp(">",Id("d"),IntLiteral(5)),Return(IntLiteral(5)))]),Block([],[Assign(Id("d"),BinaryOp("+",Id("a"),BinaryOp("*",CallExpr(SelfLiteral(),Id("func"),[]),FloatLiteral(1.2))))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,331)) 

    def test_32(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(){
                        return nil;
                    }
                    int foo(){
                        if (d >= 2) then{
                            d := d + 1;
                            if d > 5 then return 5;
                            for i := 1 to 100 do{
                                this.func();
                            }
                        }
                    }    
                }"""
        expect = str(                                                                                                                                                                                                                                                                                                                                                                                                                                               #d := d - 1 * 2 + 3 / 2 + a[23];                                        
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[],FloatType(),Block([],[Return(NullLiteral())])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp(">=",Id("d"),IntLiteral(2)),Block([],[Assign(Id("d"),BinaryOp("+",Id("d"),IntLiteral(1))),If(BinaryOp(">",Id("d"),IntLiteral(5)),Return(IntLiteral(5))),For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[CallStmt(SelfLiteral(),Id("func"),[])]))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,332)) 
    
    def test_33(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(){
                        return nil;
                    }
                    int foo(){
                        if (d >= 2) then{
                            d := d + 1;
                            if d > 5 then return 5;
                            for i := 1 to 100 do{
                                this.func();
                                break;
                                continue;
                            }
                        }
                    }    
                }"""
        expect = str(                   
            Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[],FloatType(),Block([],[Return(NullLiteral())])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp(">=",Id("d"),IntLiteral(2)),Block([],[Assign(Id("d"),BinaryOp("+",Id("d"),IntLiteral(1))),If(BinaryOp(">",Id("d"),IntLiteral(5)),Return(IntLiteral(5))),For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[CallStmt(SelfLiteral(),Id("func"),[]),Break(),Continue()]))]))]))])])                                                                                                                                                                                                                                                                                                                                                                                                                            #d := d - 1 * 2 + 3 / 2 + a[23];                                        
        )
        self.assertTrue(TestAST.test(input,expect,333)) 
    
    def test_34(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(int a; float b){
                        return 1 + 2 + a * b;
                    }
                    int foo(){
                        if (d >= 2) then{
                            d := d + 1;
                            if d > 5 then return 5;
                            for i := 1 to 100 do{
                                this.func(1,2);
                                break;
                                break;
                                continue;
                                if true then{}
                                continue;
                            }
                        }
                    }    
                }"""
        expect = str(  
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([],[Return(BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",Id("a"),Id("b"))))])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[If(BinaryOp(">=",Id("d"),IntLiteral(2)),Block([],[Assign(Id("d"),BinaryOp("+",Id("d"),IntLiteral(1))),If(BinaryOp(">",Id("d"),IntLiteral(5)),Return(IntLiteral(5))),For(Id("i"),IntLiteral(1),IntLiteral(100),True,Block([],[CallStmt(SelfLiteral(),Id("func"),[IntLiteral(1),IntLiteral(2)]),Break(),Break(),Continue(),If(BooleanLiteral(True),Block([],[])),Continue()]))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,334)) 
    
    def test_35(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(int a; float b){
                        return 1 + 2 + a * b;
                    }
                    int foo(){
                       boolean a = true || false && b == 1 >= (2 \ 45) % 10 ;
                    }    
                }"""
        expect = str(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               #true || false && b == 1 >= (2 \ 45) % 10
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([],[Return(BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",Id("a"),Id("b"))))])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("a"),BoolType(),BinaryOp(">=",BinaryOp("==",BinaryOp("&&",BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),Id("b")),IntLiteral(1)),BinaryOp("%",BinaryOp("\\",IntLiteral(2),IntLiteral(45)),IntLiteral(10))))],[]))])])  
        )
        self.assertTrue(TestAST.test(input,expect,335)) 
    
    def test_36(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(int a; float b){
                        return 1 + 2 + a * b;
                    }
                    int foo(){
                       Ex obj;
                       obj.func();
                    }    
                }"""
        expect = str(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               #true || false && b == 1 >= (2 \ 45) % 10
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([],[Return(BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",Id("a"),Id("b"))))])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("obj"),ClassType(Id("Ex")))],[CallStmt(Id("obj"),Id("func"),[])]))])])
        )
        self.assertTrue(TestAST.test(input,expect,336)) 
    
    def test_37(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(int a; float b){
                        return 1 + 2 + a * b;
                    }
                    int foo(){
                        Ex obj = new Ex();
                        Ex a = obj.func();
                    }    
                }"""
        expect = str(      
    Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([],[Return(BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",Id("a"),Id("b"))))])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("obj"),ClassType(Id("Ex")),NewExpr(Id("Ex"),[])),VarDecl(Id("a"),ClassType(Id("Ex")),CallExpr(Id("obj"),Id("func"),[]))],[]))])])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #true || false && b == 1 >= (2 \ 45) % 10
        )
        self.assertTrue(TestAST.test(input,expect,337)) 
    
    def test_38(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(int a; float b){
                        return 1 + 2 + a * b;
                    }
                    int foo(){
                        Ex obj = new Ex();
                        a := obj.func(1,2.2);
                        return a;
                    }    
                }"""
        expect = str(      
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([],[Return(BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",Id("a"),Id("b"))))])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("obj"),ClassType(Id("Ex")),NewExpr(Id("Ex"),[]))],[Assign(Id("a"),CallExpr(Id("obj"),Id("func"),[IntLiteral(1),FloatLiteral(2.2)])),Return(Id("a"))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,338))

    def test_39(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(int a; float b){
                        return this.Ex(a,b) + b*a;
                    }
                    int foo(){
                        Ex obj = new Ex();
                        a := obj.func(1,2.2);
                        return a * 2;
                    }    
                }"""
        expect = str(      
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([],[Return(BinaryOp("+",CallExpr(SelfLiteral(),Id("Ex"),[Id("a"),Id("b")]),BinaryOp("*",Id("b"),Id("a"))))])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("obj"),ClassType(Id("Ex")),NewExpr(Id("Ex"),[]))],[Assign(Id("a"),CallExpr(Id("obj"),Id("func"),[IntLiteral(1),FloatLiteral(2.2)])),Return(BinaryOp("*",Id("a"),IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,339))

    def test_40(self):
        """Simple program: class main {} """
        input = """class Ex {
                    final string a = "Hellows";
                    Ex(){
                        final int d;
                    }
                    float func(int a; float b){
                        return this.Ex(a,b);
                    }
                    int foo(){
                        Ex obj = new Ex();
                        a := new Ex().a ^ "anvn"  ^ ("a" ^ a);
                        return a * 2;
                    }    
                }"""
        expect = str(      
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([],[Return(CallExpr(SelfLiteral(),Id("Ex"),[Id("a"),Id("b")]))])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("obj"),ClassType(Id("Ex")),NewExpr(Id("Ex"),[]))],[Assign(Id("a"),BinaryOp("^",BinaryOp("^",FieldAccess(NewExpr(Id("Ex"),[]),Id("a")),StringLiteral("\"anvn\"")),BinaryOp("^",StringLiteral("\"a\""),Id("a")))),Return(BinaryOp("*",Id("a"),IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,340))
    
    def test_41(self):
        """Simple program: class main {} """
        input = """class Ex {
                        final string a = "Hellows";
                        Ex(){
                            final int d;
                        }
                        float func(int a; float b){
                            return this.Ex(a,b);
                        }
                        int foo(){
                            Ex obj = new Ex();
                            a := new Ex().a ^ "anvn"  ^ ("a" ^ a);
                            return a ;
                        }   
                    }
                         
                    class mina extends Ex{
                        #static void typesss(){break;if Break then break;}
                    }
                """
        expect = str(      
Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),ConstDecl(Id("a"),StringType(),StringLiteral("\"Hellows\""))),MethodDecl(Instance(),Id("<init>"),[],None,Block([ConstDecl(Id("d"),IntType(),None)],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],FloatType(),Block([],[Return(CallExpr(SelfLiteral(),Id("Ex"),[Id("a"),Id("b")]))])),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([VarDecl(Id("obj"),ClassType(Id("Ex")),NewExpr(Id("Ex"),[]))],[Assign(Id("a"),BinaryOp("^",BinaryOp("^",FieldAccess(NewExpr(Id("Ex"),[]),Id("a")),StringLiteral("\"anvn\"")),BinaryOp("^",StringLiteral("\"a\""),Id("a")))),Return(Id("a"))]))]),ClassDecl(Id("mina"),[],Id("Ex"))])
        )
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test_42(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 {
                    void main(){
                        Shape s;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[Assign(Id("s"),NewExpr(Id("Rectangle"),[IntLiteral(3),IntLiteral(4)])),CallStmt(Id("io"),Id("writeFloatLn"),[CallExpr(Id("s"),Id("getArea"),[])]),Assign(Id("s"),NewExpr(Id("Triangle"),[IntLiteral(3),IntLiteral(4)])),CallStmt(Id("io"),Id("writeFloatLn"),[CallExpr(Id("s"),Id("getArea"),[])])]))])])
        )
        self.assertTrue(TestAST.test(input,expect,342))
    
    def test_43(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 {
                    void main(){
                        Shape s;
                        if !nil then {}
                    }
                }
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[If(UnaryOp("!",NullLiteral()),Block([],[]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,343))
    
    def test_44(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 {
                    void main(){
                        Shape s;
                        if !nil then {
                            for i:=100000 downto 12 - 12 / 1 do{
                                s := new Shape(12,12);
                            }
                        }
                    }
                }
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[If(UnaryOp("!",NullLiteral()),Block([],[For(Id("i"),IntLiteral(100000),BinaryOp("-",IntLiteral(12),BinaryOp("/",IntLiteral(12),IntLiteral(1))),False,Block([],[Assign(Id("s"),NewExpr(Id("Shape"),[IntLiteral(12),IntLiteral(12)]))]))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test_45(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 {
                    void main(){
                        Shape s;
                        if !nil then {
                            for i:=100000 downto 12 - 12 / 1 do{
                                int a = 12;
                                final int banla = a + 11 - -12;
                                s := new Shape(12,12);

                            }
                        }
                    }
                }
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[If(UnaryOp("!",NullLiteral()),Block([],[For(Id("i"),IntLiteral(100000),BinaryOp("-",IntLiteral(12),BinaryOp("/",IntLiteral(12),IntLiteral(1))),False,Block([VarDecl(Id("a"),IntType(),IntLiteral(12)),ConstDecl(Id("banla"),IntType(),BinaryOp("-",BinaryOp("+",Id("a"),IntLiteral(11)),UnaryOp("-",IntLiteral(12))))],[Assign(Id("s"),NewExpr(Id("Shape"),[IntLiteral(12),IntLiteral(12)]))]))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,345))

    def test_46(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 {
                    void main(){
                        Shape s;
                        if !nil then {
                            for i:=100000 downto 12 - 12 / 1 do{
                                for j:= 1 to s.length() do{
                                    for o:=0 downto -10 do{
                                        io.print();
                                    }
                                }

                            }
                        }
                    }
                }
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[If(UnaryOp("!",NullLiteral()),Block([],[For(Id("i"),IntLiteral(100000),BinaryOp("-",IntLiteral(12),BinaryOp("/",IntLiteral(12),IntLiteral(1))),False,Block([],[For(Id("j"),IntLiteral(1),CallExpr(Id("s"),Id("length"),[]),True,Block([],[For(Id("o"),IntLiteral(0),UnaryOp("-",IntLiteral(10)),False,Block([],[CallStmt(Id("io"),Id("print"),[])]))]))]))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,346))
    
    def test_47(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 {
                    void main(){
                        Shape s;
                        if !nil then {
                            for i:=100000 downto 12 - 12 / 1 do{
                                if true then{} else{
                                    if false then {if true||true then {}}
                                }
                            }
                        }
                    }
                }
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[If(UnaryOp("!",NullLiteral()),Block([],[For(Id("i"),IntLiteral(100000),BinaryOp("-",IntLiteral(12),BinaryOp("/",IntLiteral(12),IntLiteral(1))),False,Block([],[If(BooleanLiteral(True),Block([],[]),Block([],[If(BooleanLiteral(False),Block([],[If(BinaryOp("||",BooleanLiteral(True),BooleanLiteral(True)),Block([],[]))]))]))]))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,347))
    
    def test_48(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 {
                    void main(){
                        Shape s;
                        for a := s.width() to s.length() do{
                            this.length[a] := s.length() + a;
                            io.print(this.length[a]);
                        }
                    }
                }
                """
        expect = str(      
            Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[For(Id("a"),CallExpr(Id("s"),Id("width"),[]),CallExpr(Id("s"),Id("length"),[]),True,Block([],[Assign(ArrayCell(FieldAccess(SelfLiteral(),Id("length")),Id("a")),BinaryOp("+",CallExpr(Id("s"),Id("length"),[]),Id("a"))),CallStmt(Id("io"),Id("print"),[ArrayCell(FieldAccess(SelfLiteral(),Id("length")),Id("a"))])]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,348))

    def test_49(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                        void func(float len, wid){
                            return this.length + new Shape(len,wid).func();
                        }
                    }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(BinaryOp("+",FieldAccess(SelfLiteral(),Id("length")),CallExpr(NewExpr(Id("Shape"),[Id("len"),Id("wid")]),Id("func"),[])))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape"))])
        )
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test_50(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        Shape(float length,width){
                            #this.length := length;
                            #this.width := width;
                        }
                        void func(float len, wid){
                            return Shape.Shape(1,2);
                        }
                    }
                class Triangle extends Shape {
                    float getArea(){
                        return a;
                    }
                }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(CallExpr(Id("Shape"),Id("Shape"),[IntLiteral(1),IntLiteral(2)]))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(Id("a"))]))],Id("Shape"))])
        )
        self.assertTrue(TestAST.test(input,expect,350))
    
    def test_51(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                        void func(float len, wid){
                            return Shape.Shape(1,2) % this.b + this.a;
                        }
                    }
                class Triangle extends Shape {
                    static float getArea(){
                        return a;
                    }
                }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(BinaryOp("+",BinaryOp("%",CallExpr(Id("Shape"),Id("Shape"),[IntLiteral(1),IntLiteral(2)]),FieldAccess(SelfLiteral(),Id("b"))),FieldAccess(SelfLiteral(),Id("a"))))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Static(),Id("getArea"),[],FloatType(),Block([],[Return(Id("a"))]))],Id("Shape"))])
        )
        self.assertTrue(TestAST.test(input,expect,351))
    
    def test_52(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            string name = "name";
                            Shape a;
                            a := new Shape();
                            this.length := length;
                            this.width := width;
                        }
                        void func(float len, wid){
                            return Shape.Shape(1,2) % this.b + --this.a;
                        }
                    }
                class Triangle extends Shape {
                    static float getArea(){
                        return nil;
                    }
                }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),StringLiteral("\"name\"")),VarDecl(Id("a"),ClassType(Id("Shape")))],[Assign(Id("a"),NewExpr(Id("Shape"),[])),Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(BinaryOp("+",BinaryOp("%",CallExpr(Id("Shape"),Id("Shape"),[IntLiteral(1),IntLiteral(2)]),FieldAccess(SelfLiteral(),Id("b"))),UnaryOp("-",UnaryOp("-",FieldAccess(SelfLiteral(),Id("a"))))))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Static(),Id("getArea"),[],FloatType(),Block([],[Return(NullLiteral())]))],Id("Shape"))])
        )
        self.assertTrue(TestAST.test(input,expect,352))
    
    def test_53(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            string name = "name";
                            Shape a;
                            {
                            a := new Shape();
                            this.length := length;
                            this.width := width;}
                        }
                        void func(float len, wid){
                            return new Shape().a[a[a[a[1+1]]]];
                        }
                    }
                class Triangle extends Shape {
                    static float getArea(){
                        return nil;
                    }
                }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),StringLiteral("\"name\"")),VarDecl(Id("a"),ClassType(Id("Shape")))],[Block([],[Assign(Id("a"),NewExpr(Id("Shape"),[])),Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))])])),MethodDecl(Instance(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(ArrayCell(FieldAccess(NewExpr(Id("Shape"),[]),Id("a")),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(1)))))))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Static(),Id("getArea"),[],FloatType(),Block([],[Return(NullLiteral())]))],Id("Shape"))])
        )
        self.assertTrue(TestAST.test(input,expect,353))
    
    def test_54(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            string name = "name";
                            Shape a;
                            {{}{}{}
                            a := new Shape();
                            this.length := length;
                            a := this.a.b.c.d[1] + this.e().f().g;
                            this.width := width;}
                        }
                        static void func(float len, wid){
                            return new Shape().a[a[a[a[1+1]]]];
                        }
                    }
                class Triangle extends Shape {
                    static float getArea(){
                        return nil; return a;
                    }
                }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),StringLiteral("\"name\"")),VarDecl(Id("a"),ClassType(Id("Shape")))],[Block([],[Block([],[]),Block([],[]),Block([],[]),Assign(Id("a"),NewExpr(Id("Shape"),[])),Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(Id("a"),BinaryOp("+",ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(SelfLiteral(),Id("a")),Id("b")),Id("c")),Id("d")),IntLiteral(1)),FieldAccess(CallExpr(CallExpr(SelfLiteral(),Id("e"),[]),Id("f"),[]),Id("g")))),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))])])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(ArrayCell(FieldAccess(NewExpr(Id("Shape"),[]),Id("a")),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(1)))))))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Static(),Id("getArea"),[],FloatType(),Block([],[Return(NullLiteral()),Return(Id("a"))]))],Id("Shape"))])
        )
        self.assertTrue(TestAST.test(input,expect,354))
    
    def test_55(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            string name = "name";
                            Shape a;
                            
                        }
                        static void func(float len, wid){
                            float len = len;
                            wied := 122 +331 - --------------1;
                            return new Shape().a[a[a[a[1+1]]]];
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),StringLiteral("\"name\"")),VarDecl(Id("a"),ClassType(Id("Shape")))],[])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([VarDecl(Id("len"),FloatType(),Id("len"))],[Assign(Id("wied"),BinaryOp("-",BinaryOp("+",IntLiteral(122),IntLiteral(331)),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(1))))))))))))))))),Return(ArrayCell(FieldAccess(NewExpr(Id("Shape"),[]),Id("a")),ArrayCell(Id("a"),ArrayCell(Id("a"),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(1)))))))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,355))
    
    def test_56(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            string name = "name";
                            Shape a;
                            
                            a := new Shape();
                            this.length := length;
                            a := this.a.b.c.d[1] + this.e().f().g;
                            this.width := width;
                        }
                        static void func(float len, wid){
                            return 1 % 2 +3 != true;
                        }
                    }
                class Triangle extends Shape {
                    static float getArea(){
                        return nil; return a;
                    }
                }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),StringLiteral("\"name\"")),VarDecl(Id("a"),ClassType(Id("Shape")))],[Assign(Id("a"),NewExpr(Id("Shape"),[])),Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(Id("a"),BinaryOp("+",ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(SelfLiteral(),Id("a")),Id("b")),Id("c")),Id("d")),IntLiteral(1)),FieldAccess(CallExpr(CallExpr(SelfLiteral(),Id("e"),[]),Id("f"),[]),Id("g")))),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(BinaryOp("!=",BinaryOp("+",BinaryOp("%",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BooleanLiteral(True)))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Static(),Id("getArea"),[],FloatType(),Block([],[Return(NullLiteral()),Return(Id("a"))]))],Id("Shape"))])
        )
        self.assertTrue(TestAST.test(input,expect,356))
    
    def test_57(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            string name = "name";
                            Shape a;
                            int[12] array = {1,2,3,4,5,6,7,8,9};
                            array[11] := nil;
                        }
                        static void func(float len, wid){
                            return 1 % 2 +3 != true;
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),StringLiteral("\"name\"")),VarDecl(Id("a"),ClassType(Id("Shape"))),VarDecl(Id("array"),ArrayType(12,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9)]))],[Assign(ArrayCell(Id("array"),IntLiteral(11)),NullLiteral())])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(BinaryOp("!=",BinaryOp("+",BinaryOp("%",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BooleanLiteral(True)))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,357))
    
    def test_58(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            string name = "name";
                            Shape a;
                            int[12] array, arr, lis;
                            array := {1,2,3};
                            array[11] := nil;
                            lis := arr;
                            arr := lis + array;
                        }
                        static void func(float len, wid){
                            return true || false && (12 + 11%3);
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),StringLiteral("\"name\"")),VarDecl(Id("a"),ClassType(Id("Shape"))),VarDecl(Id("array"),ArrayType(12,IntType())),VarDecl(Id("arr"),ArrayType(12,IntType())),VarDecl(Id("lis"),ArrayType(12,IntType()))],[Assign(Id("array"),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])),Assign(ArrayCell(Id("array"),IntLiteral(11)),NullLiteral()),Assign(Id("lis"),Id("arr")),Assign(Id("arr"),BinaryOp("+",Id("lis"),Id("array")))])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(BinaryOp("&&",BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),BinaryOp("+",IntLiteral(12),BinaryOp("%",IntLiteral(11),IntLiteral(3)))))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,358))

    def test_59(self):
        """Simple program: class main {} """
        input = """class Shape {
                        static string funcc(int len, str; boolean po){
                            return true && true;
                        }
                        float length,width; int a; final static float b;
                        Shape(float length,width){
                            string name = "name" ^ a ^ this.length();
                        }
                        static void func(float len, wid){
                            return true || false && (12 + 11%3);
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[MethodDecl(Static(),Id("funcc"),[VarDecl(Id("len"),IntType()),VarDecl(Id("str"),IntType()),VarDecl(Id("po"),BoolType())],StringType(),Block([],[Return(BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(True)))])),AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),BinaryOp("^",BinaryOp("^",StringLiteral("\"name\""),Id("a")),CallExpr(SelfLiteral(),Id("length"),[])))],[])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(BinaryOp("&&",BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),BinaryOp("+",IntLiteral(12),BinaryOp("%",IntLiteral(11),IntLiteral(3)))))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,359))
    
    def test_60(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; 
                        int a; 
                        final static float b;
                        Shape(float length,width){
                            string name = "name" ^ a ^ this.length();
                        }
                        static void func(float len, wid){
                            return obj.func(len+1, wid-1);
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),BinaryOp("^",BinaryOp("^",StringLiteral("\"name\""),Id("a")),CallExpr(SelfLiteral(),Id("length"),[])))],[])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([],[Return(CallExpr(Id("obj"),Id("func"),[BinaryOp("+",Id("len"),IntLiteral(1)),BinaryOp("-",Id("wid"),IntLiteral(1))]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,360))
    
    def test_61(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; 
                        int a; 
                        final static float b;
                        Shape(float length,width){
                            string name = "name" ^ a ^ this.length();
                        }
                        static void func(float len, wid){
                            final Shape a,b=new Shape(),ve,ad=new Shape(12,12);
                            return obj.func(len+1, wid-1) + ad.length[100];
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),BinaryOp("^",BinaryOp("^",StringLiteral("\"name\""),Id("a")),CallExpr(SelfLiteral(),Id("length"),[])))],[])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType())],VoidType(),Block([ConstDecl(Id("a"),ClassType(Id("Shape")),None),ConstDecl(Id("b"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[])),ConstDecl(Id("ve"),ClassType(Id("Shape")),None),ConstDecl(Id("ad"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[IntLiteral(12),IntLiteral(12)]))],[Return(BinaryOp("+",CallExpr(Id("obj"),Id("func"),[BinaryOp("+",Id("len"),IntLiteral(1)),BinaryOp("-",Id("wid"),IntLiteral(1))]),ArrayCell(FieldAccess(Id("ad"),Id("length")),IntLiteral(100))))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,361))
    
    def test_62(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; 
                        int a; 
                        boolean boo;
                        final static float b;
                        Shape(float length,width){
                            string name = "name" ^ a ^ this.length();
                        }
                        static void func(float len, wid; Shape a,b){
                            final Shape a,b=new Shape(),ve,ad=new Shape(12,12);
                            a := b.lenght().func();
                            return obj.func(len+1, wid-1) + ad.length[100];
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("boo"),BoolType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),BinaryOp("^",BinaryOp("^",StringLiteral("\"name\""),Id("a")),CallExpr(SelfLiteral(),Id("length"),[])))],[])),MethodDecl(Static(),Id("func"),[VarDecl(Id("len"),FloatType()),VarDecl(Id("wid"),FloatType()),VarDecl(Id("a"),ClassType(Id("Shape"))),VarDecl(Id("b"),ClassType(Id("Shape")))],VoidType(),Block([ConstDecl(Id("a"),ClassType(Id("Shape")),None),ConstDecl(Id("b"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[])),ConstDecl(Id("ve"),ClassType(Id("Shape")),None),ConstDecl(Id("ad"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[IntLiteral(12),IntLiteral(12)]))],[Assign(Id("a"),CallExpr(CallExpr(Id("b"),Id("lenght"),[]),Id("func"),[])),Return(BinaryOp("+",CallExpr(Id("obj"),Id("func"),[BinaryOp("+",Id("len"),IntLiteral(1)),BinaryOp("-",Id("wid"),IntLiteral(1))]),ArrayCell(FieldAccess(Id("ad"),Id("length")),IntLiteral(100))))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,362))
    
    def test_63(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; 
                        int a; 
                        boolean boo;
                        final static float b;
                        Shape(float length,width){
                            string name = "name" ^ a ^ this.length();
                            return new Shape();
                        }
                        int main(){
                            io.println("this is a string");
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("boo"),BoolType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),BinaryOp("^",BinaryOp("^",StringLiteral("\"name\""),Id("a")),CallExpr(SelfLiteral(),Id("length"),[])))],[Return(NewExpr(Id("Shape"),[]))])),MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[CallStmt(Id("io"),Id("println"),[StringLiteral("\"this is a string\"")])]))])])
        )
        self.assertTrue(TestAST.test(input,expect,363))
    
    def test_64(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width; 
                        int a; 
                        boolean boo;
                        final static float b;
                        Shape(float length,width){
                            string name = "name" ^ a ^ this.length();
                            return new Shape();
                        }
                        int main(){
                            io.println("this is a string " + this.a + " with value a");
                            return nil;
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),VarDecl(Id("boo"),BoolType())),AttributeDecl(Static(),ConstDecl(Id("b"),FloatType(),None)),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([VarDecl(Id("name"),StringType(),BinaryOp("^",BinaryOp("^",StringLiteral("\"name\""),Id("a")),CallExpr(SelfLiteral(),Id("length"),[])))],[Return(NewExpr(Id("Shape"),[]))])),MethodDecl(Instance(),Id("main"),[],IntType(),Block([],[CallStmt(Id("io"),Id("println"),[BinaryOp("+",BinaryOp("+",StringLiteral("\"this is a string \""),FieldAccess(SelfLiteral(),Id("a"))),StringLiteral("\" with value a\""))]),Return(NullLiteral())]))])])
        )
        self.assertTrue(TestAST.test(input,expect,364)) 
    

    def test_65(self):
        """Simple program: class main {} """
        input = """class Fraction {
                        int deno;
                        int nume;
                        int gcd(int a,b){
                            if b == 0 then
                                return a;
                            else return this.gcd(b, a % b);

                        }

                        Fraction(int a,b){
                            this.deno := a / this.gcd(a,b);
                            this.nume := b / this.gcd(a,b);
                        }
                        
                        plusoperator(Fraction rhs){
                            a := this.deno * rhs.nume + rhs.deno * this.nume;
                            b := this.nume * rhs.nume;
                            return this.Fraction(a,b);
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Fraction"),[AttributeDecl(Instance(),VarDecl(Id("deno"),IntType())),AttributeDecl(Instance(),VarDecl(Id("nume"),IntType())),MethodDecl(Instance(),Id("gcd"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([],[If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(Id("a")),Return(CallExpr(SelfLiteral(),Id("gcd"),[Id("b"),BinaryOp("%",Id("a"),Id("b"))])))])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("deno")),BinaryOp("/",Id("a"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")]))),Assign(FieldAccess(SelfLiteral(),Id("nume")),BinaryOp("/",Id("b"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")])))])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],None,Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("nume"))),BinaryOp("*",FieldAccess(Id("rhs"),Id("deno")),FieldAccess(SelfLiteral(),Id("nume"))))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,365)) 
    
    def test_66(self):
        """Simple program: class main {} """
        input = """class Fraction {
                        int deno;
                        int nume;
                        int gcd(int a,b){
                            if b == 0 then
                                return a;
                            else return this.gcd(b, a % b);

                        }

                        Fraction(int a,b){
                            this.deno := a / this.gcd(a,b);
                            this.nume := b / this.gcd(a,b);
                        }
                        
                        Fraction plusoperator(Fraction rhs){
                            a := this.deno * rhs.nume + rhs.deno * this.nume;
                            b := this.nume * rhs.nume;
                            return this.Fraction(a,b);
                        }

                        Fraction suboperator(Fraction rhs){
                            a := this.deno * rhs.nume - rhs.deno * this.nume;
                            b := this.nume * rhs.nume;
                            return this.Fraction(a,b);
                        }

                        Fraction muloperator(Fraction rhs){
                            a := this.deno * rhs.deno ;
                            b := this.nume * rhs.nume;
                            return this.Fraction(a,b);
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Fraction"),[AttributeDecl(Instance(),VarDecl(Id("deno"),IntType())),AttributeDecl(Instance(),VarDecl(Id("nume"),IntType())),MethodDecl(Instance(),Id("gcd"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([],[If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(Id("a")),Return(CallExpr(SelfLiteral(),Id("gcd"),[Id("b"),BinaryOp("%",Id("a"),Id("b"))])))])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("deno")),BinaryOp("/",Id("a"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")]))),Assign(FieldAccess(SelfLiteral(),Id("nume")),BinaryOp("/",Id("b"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")])))])),MethodDecl(Instance(),Id("plusoperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("nume"))),BinaryOp("*",FieldAccess(Id("rhs"),Id("deno")),FieldAccess(SelfLiteral(),Id("nume"))))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]))])),MethodDecl(Instance(),Id("suboperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[Assign(Id("a"),BinaryOp("-",BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("nume"))),BinaryOp("*",FieldAccess(Id("rhs"),Id("deno")),FieldAccess(SelfLiteral(),Id("nume"))))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]))])),MethodDecl(Instance(),Id("muloperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[Assign(Id("a"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("deno")))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,366)) 

    def test_67(self):
        """Simple program: class main {} """
        input = """class Fraction {
                        int deno;
                        int nume;
                        int gcd(int a,b){
                            if b == 0 then
                                return a;
                            else return this.gcd(b, a % b);

                        }

                        Fraction(int a,b){
                            this.deno := a / this.gcd(a,b);
                            this.nume := b / this.gcd(a,b);
                        }
                        
                        static Fraction plusoperator(Fraction rhs){
                            if b == 0 then return nil;
                            else{
                                a := this.deno * rhs.nume + rhs.deno * this.nume;
                                b := this.nume * rhs.nume;
                                return this.Fraction(a,b);
                            }
                        }

                        static Fraction suboperator(Fraction rhs){
                            if b != 0 then{
                                a := this.deno * rhs.nume - rhs.deno * this.nume;
                                b := this.nume * rhs.nume;
                                return this.Fraction(a,b).gcd();
                            }
                            else return nil; 
                        }

                        static Fraction muloperator(Fraction rhs){
                            a := this.deno * rhs.deno ;
                            b := this.nume * rhs.nume;
                            return this.Fraction(a,b) + this.Fraction(a,b*2);
                        }
                    }
                
                """
        expect = str(      
Program([ClassDecl(Id("Fraction"),[AttributeDecl(Instance(),VarDecl(Id("deno"),IntType())),AttributeDecl(Instance(),VarDecl(Id("nume"),IntType())),MethodDecl(Instance(),Id("gcd"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([],[If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(Id("a")),Return(CallExpr(SelfLiteral(),Id("gcd"),[Id("b"),BinaryOp("%",Id("a"),Id("b"))])))])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("deno")),BinaryOp("/",Id("a"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")]))),Assign(FieldAccess(SelfLiteral(),Id("nume")),BinaryOp("/",Id("b"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")])))])),MethodDecl(Static(),Id("plusoperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(NullLiteral()),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("nume"))),BinaryOp("*",FieldAccess(Id("rhs"),Id("deno")),FieldAccess(SelfLiteral(),Id("nume"))))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]))]))])),MethodDecl(Static(),Id("suboperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[If(BinaryOp("!=",Id("b"),IntLiteral(0)),Block([],[Assign(Id("a"),BinaryOp("-",BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("nume"))),BinaryOp("*",FieldAccess(Id("rhs"),Id("deno")),FieldAccess(SelfLiteral(),Id("nume"))))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]),Id("gcd"),[]))]),Return(NullLiteral()))])),MethodDecl(Static(),Id("muloperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[Assign(Id("a"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("deno")))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(BinaryOp("+",CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]),CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),BinaryOp("*",Id("b"),IntLiteral(2))])))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,367)) 
    

    def test_68(self):
        """Simple program: class main {} """
        input = """class Fraction extends Expr{
                        int deno;
                        int nume;
                        int gcd(int a,b){
                            if b == 0 then
                                return a;
                            else return this.gcd(b, a % b);

                        }

                        Fraction(int a,b){
                            this.deno := a / this.gcd(a,b);
                            this.nume := b / this.gcd(a,b);
                        }
                        
                        static Fraction plusoperator(Fraction rhs){
                            if b == 0 then return nil;
                            else{
                                a := this.deno * rhs.nume + rhs.deno * this.nume;
                                b := this.nume * rhs.nume;
                                return this.Fraction(a,b);
                            }
                        }

                        static Fraction suboperator(Fraction rhs){
                            if b != 0 then{
                                a := this.deno * rhs.nume - rhs.deno * this.nume;
                                b := this.nume * rhs.nume;
                                return this.Fraction(a,b).gcd();
                            }
                            else return nil; 
                        }

                        static Fraction muloperator(Fraction rhs){
                            a := this.deno * rhs.deno ;
                            b := this.nume * rhs.nume;
                            return this.Fraction(a,b) + this.Fraction(a,b*2);
                        }
                    }

                    class Expr{
                        Expr lhs, rhs;
                        Expr(string op; Expr lhs, rhs){
                            return this.Binary(op, lhs,rhs);
                        }
                    }
                """
        expect = str(      
Program([ClassDecl(Id("Fraction"),[AttributeDecl(Instance(),VarDecl(Id("deno"),IntType())),AttributeDecl(Instance(),VarDecl(Id("nume"),IntType())),MethodDecl(Instance(),Id("gcd"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([],[If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(Id("a")),Return(CallExpr(SelfLiteral(),Id("gcd"),[Id("b"),BinaryOp("%",Id("a"),Id("b"))])))])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("deno")),BinaryOp("/",Id("a"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")]))),Assign(FieldAccess(SelfLiteral(),Id("nume")),BinaryOp("/",Id("b"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")])))])),MethodDecl(Static(),Id("plusoperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(NullLiteral()),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("nume"))),BinaryOp("*",FieldAccess(Id("rhs"),Id("deno")),FieldAccess(SelfLiteral(),Id("nume"))))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]))]))])),MethodDecl(Static(),Id("suboperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[If(BinaryOp("!=",Id("b"),IntLiteral(0)),Block([],[Assign(Id("a"),BinaryOp("-",BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("nume"))),BinaryOp("*",FieldAccess(Id("rhs"),Id("deno")),FieldAccess(SelfLiteral(),Id("nume"))))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]),Id("gcd"),[]))]),Return(NullLiteral()))])),MethodDecl(Static(),Id("muloperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[Assign(Id("a"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("deno")))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(BinaryOp("+",CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]),CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),BinaryOp("*",Id("b"),IntLiteral(2))])))]))],Id("Expr")),ClassDecl(Id("Expr"),[AttributeDecl(Instance(),VarDecl(Id("lhs"),ClassType(Id("Expr")))),AttributeDecl(Instance(),VarDecl(Id("rhs"),ClassType(Id("Expr")))),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("op"),StringType()),VarDecl(Id("lhs"),ClassType(Id("Expr"))),VarDecl(Id("rhs"),ClassType(Id("Expr")))],None,Block([],[Return(CallExpr(SelfLiteral(),Id("Binary"),[Id("op"),Id("lhs"),Id("rhs")]))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,368)) 
    
    def test_69(self):
        """Simple program: class main {} """
        input = """class Fraction extends Expr{
                        int deno;
                        int nume;
                        static int all = 0;

                        int gcd(int a,b){
                            if b == 0 then
                                return a;
                            else return this.gcd(b, a % b);

                        }

                        Fraction(int a,b){
                            this.deno := a / this.gcd(a,b);
                            this.nume := b / this.gcd(a,b);
                            this.all := this.all + 1;
                        }
                        
                        static Fraction plusoperator(Fraction rhs){
                            if b == 0 then return nil;
                            else{
                                a := this.deno * rhs.nume + rhs.deno * this.nume;
                                b := this.nume * rhs.nume;
                                return this.Fraction(a,b);
                            }
                            for i:=0 to this.all do{
                                #io.print("this is the " + i  + "element");
                                if i <= -1 then break; else continue;
                            }
                        }

                       
                    }

                    
                """
        expect = str(      
Program([ClassDecl(Id("Fraction"),[AttributeDecl(Instance(),VarDecl(Id("deno"),IntType())),AttributeDecl(Instance(),VarDecl(Id("nume"),IntType())),AttributeDecl(Static(),VarDecl(Id("all"),IntType(),IntLiteral(0))),MethodDecl(Instance(),Id("gcd"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],IntType(),Block([],[If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(Id("a")),Return(CallExpr(SelfLiteral(),Id("gcd"),[Id("b"),BinaryOp("%",Id("a"),Id("b"))])))])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("deno")),BinaryOp("/",Id("a"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")]))),Assign(FieldAccess(SelfLiteral(),Id("nume")),BinaryOp("/",Id("b"),CallExpr(SelfLiteral(),Id("gcd"),[Id("a"),Id("b")]))),Assign(FieldAccess(SelfLiteral(),Id("all")),BinaryOp("+",FieldAccess(SelfLiteral(),Id("all")),IntLiteral(1)))])),MethodDecl(Static(),Id("plusoperator"),[VarDecl(Id("rhs"),ClassType(Id("Fraction")))],ClassType(Id("Fraction")),Block([],[If(BinaryOp("==",Id("b"),IntLiteral(0)),Return(NullLiteral()),Block([],[Assign(Id("a"),BinaryOp("+",BinaryOp("*",FieldAccess(SelfLiteral(),Id("deno")),FieldAccess(Id("rhs"),Id("nume"))),BinaryOp("*",FieldAccess(Id("rhs"),Id("deno")),FieldAccess(SelfLiteral(),Id("nume"))))),Assign(Id("b"),BinaryOp("*",FieldAccess(SelfLiteral(),Id("nume")),FieldAccess(Id("rhs"),Id("nume")))),Return(CallExpr(SelfLiteral(),Id("Fraction"),[Id("a"),Id("b")]))])),For(Id("i"),IntLiteral(0),FieldAccess(SelfLiteral(),Id("all")),True,Block([],[If(BinaryOp("<=",Id("i"),UnaryOp("-",IntLiteral(1))),Break(),Continue())]))]))],Id("Expr"))])
        )
        self.assertTrue(TestAST.test(input,expect,369)) 
    
    def test_70(self):
        """Simple program: class main {} """
        input = """class Mat extends Expr{
                        int row;
                        int column;

                        Mat(int row, column){
                            
                        }
                        
                        float Det(){

                        }

                        Mat Multi(){

                        }
                        
                       
                    }

                    
                """
        expect = str(      
Program([ClassDecl(Id("Mat"),[AttributeDecl(Instance(),VarDecl(Id("row"),IntType())),AttributeDecl(Instance(),VarDecl(Id("column"),IntType())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("row"),IntType()),VarDecl(Id("column"),IntType())],None,Block([],[])),MethodDecl(Instance(),Id("Det"),[],FloatType(),Block([],[])),MethodDecl(Instance(),Id("Multi"),[],ClassType(Id("Mat")),Block([],[]))],Id("Expr"))])
        )
        self.assertTrue(TestAST.test(input,expect,370)) 

    def test_71(self):
        """Simple program: class main {} """
        input = """class Mat extends Expr{
                        int row;
                        int column;
                        int[100] val;

                        Mat(int row, column){
                            this.row := row;
                            this.column := column;
                            for i:=0 to this.row do{
                                for j:=0 to this.column do{
                                    nu := io.scan();
                                    val[i*this.column + j] := nu;
                                }
                            }
                        }
                        
                        float Det(){
                            return nil;
                        }

                        Mat Multi(Mat rhs){
                            return this * rhs;
                        }
                        
                       
                    }

                    
                """
        expect = str(      
Program([ClassDecl(Id("Mat"),[AttributeDecl(Instance(),VarDecl(Id("row"),IntType())),AttributeDecl(Instance(),VarDecl(Id("column"),IntType())),AttributeDecl(Instance(),VarDecl(Id("val"),ArrayType(100,IntType()))),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("row"),IntType()),VarDecl(Id("column"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("row")),Id("row")),Assign(FieldAccess(SelfLiteral(),Id("column")),Id("column")),For(Id("i"),IntLiteral(0),FieldAccess(SelfLiteral(),Id("row")),True,Block([],[For(Id("j"),IntLiteral(0),FieldAccess(SelfLiteral(),Id("column")),True,Block([],[Assign(Id("nu"),CallExpr(Id("io"),Id("scan"),[])),Assign(ArrayCell(Id("val"),BinaryOp("+",BinaryOp("*",Id("i"),FieldAccess(SelfLiteral(),Id("column"))),Id("j"))),Id("nu"))]))]))])),MethodDecl(Instance(),Id("Det"),[],FloatType(),Block([],[Return(NullLiteral())])),MethodDecl(Instance(),Id("Multi"),[VarDecl(Id("rhs"),ClassType(Id("Mat")))],ClassType(Id("Mat")),Block([],[Return(BinaryOp("*",SelfLiteral(),Id("rhs")))]))],Id("Expr"))])
        )
        self.assertTrue(TestAST.test(input,expect,371)) 
    
    def test_72(self):
        """Simple program: class main {} """
        input = """class Node extends List{
                        int val;
                        Node next;
                        int getVal(){
                            return this.val;
                        }

                        void setVal(int val){
                            this.val := val;
                        }

                        boolean deleteNode(){}
                    }

                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType())),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")))),MethodDecl(Instance(),Id("getVal"),[],IntType(),Block([],[Return(FieldAccess(SelfLiteral(),Id("val")))])),MethodDecl(Instance(),Id("setVal"),[VarDecl(Id("val"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("deleteNode"),[],BoolType(),Block([],[]))],Id("List"))])
        )
        self.assertTrue(TestAST.test(input,expect,372))

    def test_73(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        Node(int val){
                            this.val := val;
                        }

                        int getVal(){
                            return this.val;
                        }

                        void setVal(int val){
                            this.val := val;
                        }

                        boolean deleteNode(){
                            this.next := nil;
                            this.val := 0;
                        }
                    }

                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("val"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("getVal"),[],IntType(),Block([],[Return(FieldAccess(SelfLiteral(),Id("val")))])),MethodDecl(Instance(),Id("setVal"),[VarDecl(Id("val"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("deleteNode"),[],BoolType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("next")),NullLiteral()),Assign(FieldAccess(SelfLiteral(),Id("val")),IntLiteral(0))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,373)) 
    

    def test_74(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        Node(int val){
                            this.val := val;
                        }

                        int getVal(){
                            return this.val;
                        }

                        void setVal(int val){
                            this.val := val;
                        }

                        boolean deleteNode(){
                            this.next := nil;
                            this.val := 0;
                        }
                    }

                class List {
                    Node head;
                    Node tail;
                    int size = 0;

                    List(int num){
                        Node ele;
                        this.head := ele;
                        this.tail := ele;
                        this.size := this.size + 1;
                        this.head.val := num;
                        return this.head;
                    }
                }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("val"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("getVal"),[],IntType(),Block([],[Return(FieldAccess(SelfLiteral(),Id("val")))])),MethodDecl(Instance(),Id("setVal"),[VarDecl(Id("val"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("deleteNode"),[],BoolType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("next")),NullLiteral()),Assign(FieldAccess(SelfLiteral(),Id("val")),IntLiteral(0))]))]),ClassDecl(Id("List"),[AttributeDecl(Instance(),VarDecl(Id("head"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("tail"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("size"),IntType(),IntLiteral(0))),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("num"),IntType())],None,Block([VarDecl(Id("ele"),ClassType(Id("Node")))],[Assign(FieldAccess(SelfLiteral(),Id("head")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("tail")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("+",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1))),Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("head")),Id("val")),Id("num")),Return(FieldAccess(SelfLiteral(),Id("head")))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,374)) 
    
    def test_75(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        Node(int val){
                            this.val := val;
                        }

                        int getVal(){
                            return this.val;
                        }

                        void setVal(int val){
                            this.val := val;
                        }

                        boolean deleteNode(){
                            this.next := nil;
                            this.val := 0;
                        }
                    }

                class List {
                    Node head;
                    Node tail;
                    int size = 0;

                    List(int num){
                        Node ele;
                        this.head := ele;
                        this.tail := ele;
                        this.size := this.size + 1;
                        this.head.val := num;
                        return this.head;
                    }

                    void append(int num){
                        Node ele = new Node(num);
                        this.tail.next := ele;
                        this.tail := this.tail.next;
                        this.size := this.size + 1;
                    }

                    void pop(){
                        Node ptr = this.head;
                        for i := 0 to this.size do{
                            if i == this.size - 1 then{
                                ptr.next := nil;
                                break;
                            }
                            else ptr := ptr.next;
                        }
                        this.tail.deleteNode();
                        this.tail := ptr;
                    }
                }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("val"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("getVal"),[],IntType(),Block([],[Return(FieldAccess(SelfLiteral(),Id("val")))])),MethodDecl(Instance(),Id("setVal"),[VarDecl(Id("val"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("deleteNode"),[],BoolType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("next")),NullLiteral()),Assign(FieldAccess(SelfLiteral(),Id("val")),IntLiteral(0))]))]),ClassDecl(Id("List"),[AttributeDecl(Instance(),VarDecl(Id("head"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("tail"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("size"),IntType(),IntLiteral(0))),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("num"),IntType())],None,Block([VarDecl(Id("ele"),ClassType(Id("Node")))],[Assign(FieldAccess(SelfLiteral(),Id("head")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("tail")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("+",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1))),Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("head")),Id("val")),Id("num")),Return(FieldAccess(SelfLiteral(),Id("head")))])),MethodDecl(Instance(),Id("append"),[VarDecl(Id("num"),IntType())],VoidType(),Block([VarDecl(Id("ele"),ClassType(Id("Node")),NewExpr(Id("Node"),[Id("num")]))],[Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("tail")),Id("next")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("tail")),FieldAccess(FieldAccess(SelfLiteral(),Id("tail")),Id("next"))),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("+",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1)))])),MethodDecl(Instance(),Id("pop"),[],VoidType(),Block([VarDecl(Id("ptr"),ClassType(Id("Node")),FieldAccess(SelfLiteral(),Id("head")))],[For(Id("i"),IntLiteral(0),FieldAccess(SelfLiteral(),Id("size")),True,Block([],[If(BinaryOp("==",Id("i"),BinaryOp("-",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1))),Block([],[Assign(FieldAccess(Id("ptr"),Id("next")),NullLiteral()),Break()]),Assign(Id("ptr"),FieldAccess(Id("ptr"),Id("next"))))])),CallStmt(FieldAccess(SelfLiteral(),Id("tail")),Id("deleteNode"),[]),Assign(FieldAccess(SelfLiteral(),Id("tail")),Id("ptr"))]))])])
        )
        self.assertTrue(TestAST.test(input,expect,375)) 
    

    def test_76(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        Node(int val){
                            this.val := val;
                        }

                        int getVal(){
                            return this.val;
                        }

                        void setVal(int val){
                            this.val := val;
                        }

                        boolean deleteNode(){
                            this.next := nil;
                            this.val := 0;
                        }
                    }

                class List {
                    Node head;
                    Node tail;
                    int size = 0;

                    List(int num){
                        Node ele;
                        this.head := ele;
                        this.tail := ele;
                        this.size := this.size + 1;
                        this.head.val := num;
                        return this.head;
                    }

                    void append(int num){
                        Node ele = new Node(num);
                        this.tail.next := ele;
                        this.tail := this.tail.next;
                        this.size := this.size + 1;
                    }

                    void pop(){
                        Node ptr = this.head;
                        for i := 0 to this.size do{
                            if i == this.size - 1 then{
                                ptr.next := nil;
                                break;
                            }
                            else ptr := ptr.next;
                        }
                        this.tail.deleteNode();
                        this.tail := ptr;
                        this.size := this.size - 1;
                    }

                    boolean isEmpty(){
                        if this.size == 0 then return true;
                        else return false;
                    }

                    void Empty(){
                        Node ptr = this.tail;
                        for i:=0 to this.size do{
                                {}{}
                        }
                        this.size := 0;
                        this.tail := nil;
                        this.head := nil;
                    }

                }

                class Stack extends List{}
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("val"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("getVal"),[],IntType(),Block([],[Return(FieldAccess(SelfLiteral(),Id("val")))])),MethodDecl(Instance(),Id("setVal"),[VarDecl(Id("val"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("deleteNode"),[],BoolType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("next")),NullLiteral()),Assign(FieldAccess(SelfLiteral(),Id("val")),IntLiteral(0))]))]),ClassDecl(Id("List"),[AttributeDecl(Instance(),VarDecl(Id("head"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("tail"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("size"),IntType(),IntLiteral(0))),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("num"),IntType())],None,Block([VarDecl(Id("ele"),ClassType(Id("Node")))],[Assign(FieldAccess(SelfLiteral(),Id("head")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("tail")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("+",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1))),Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("head")),Id("val")),Id("num")),Return(FieldAccess(SelfLiteral(),Id("head")))])),MethodDecl(Instance(),Id("append"),[VarDecl(Id("num"),IntType())],VoidType(),Block([VarDecl(Id("ele"),ClassType(Id("Node")),NewExpr(Id("Node"),[Id("num")]))],[Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("tail")),Id("next")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("tail")),FieldAccess(FieldAccess(SelfLiteral(),Id("tail")),Id("next"))),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("+",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1)))])),MethodDecl(Instance(),Id("pop"),[],VoidType(),Block([VarDecl(Id("ptr"),ClassType(Id("Node")),FieldAccess(SelfLiteral(),Id("head")))],[For(Id("i"),IntLiteral(0),FieldAccess(SelfLiteral(),Id("size")),True,Block([],[If(BinaryOp("==",Id("i"),BinaryOp("-",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1))),Block([],[Assign(FieldAccess(Id("ptr"),Id("next")),NullLiteral()),Break()]),Assign(Id("ptr"),FieldAccess(Id("ptr"),Id("next"))))])),CallStmt(FieldAccess(SelfLiteral(),Id("tail")),Id("deleteNode"),[]),Assign(FieldAccess(SelfLiteral(),Id("tail")),Id("ptr")),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("-",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1)))])),MethodDecl(Instance(),Id("isEmpty"),[],BoolType(),Block([],[If(BinaryOp("==",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(0)),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),MethodDecl(Instance(),Id("Empty"),[],VoidType(),Block([VarDecl(Id("ptr"),ClassType(Id("Node")),FieldAccess(SelfLiteral(),Id("tail")))],[For(Id("i"),IntLiteral(0),FieldAccess(SelfLiteral(),Id("size")),True,Block([],[Block([],[]),Block([],[])])),Assign(FieldAccess(SelfLiteral(),Id("size")),IntLiteral(0)),Assign(FieldAccess(SelfLiteral(),Id("tail")),NullLiteral()),Assign(FieldAccess(SelfLiteral(),Id("head")),NullLiteral())]))]),ClassDecl(Id("Stack"),[],Id("List"))])
        )
        self.assertTrue(TestAST.test(input,expect,376))
    

    def test_77(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        Node(int val){
                            this.val := val;
                        }

                        int getVal(){
                            return this.val;
                        }

                        void setVal(int val){
                            this.val := val;
                        }

                        boolean deleteNode(){
                            this.next := nil;
                            this.val := 0;
                        }
                    }

                class List {
                    Node head;
                    Node tail;
                    int size = 0;

                    List(int num){
                        Node ele;
                        this.head := ele;
                        this.tail := ele;
                        this.size := this.size + 1;
                        this.head.val := num;
                        return this.head;
                    }

                    void append(int num){
                        Node ele = new Node(num);
                        this.tail.next := ele;
                        this.tail := this.tail.next;
                        this.size := this.size + 1;
                    }

                    void pop(){
                        Node ptr = this.head;
                        for i := 0 to this.size do{
                            if i == this.size - 1 then{
                                ptr.next := nil;
                                break;
                            }
                            else ptr := ptr.next;
                        }
                        this.tail.deleteNode();
                        this.tail := ptr;
                        this.size := this.size - 1;
                    }

                    boolean isEmpty(){
                        if this.size == 0 then return true;
                        else return false;
                    }

                    void Empty(){
                        Node ptr = this.tail;
                        for i:=0 to this.size do{
                                {}{}
                        }
                        this.size := 0;
                        this.tail := nil;
                        this.head := nil;
                    }
                    void main(){
                        List lis = new List(1);
                        int[100] arr = {1,2,3,4,5,6,7,8,9,19};
                        for i :=0 to 100 do{
                            lis.append(arr[i]);
                        }
                        io.print(lis.size);
                    }

                }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("val"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("getVal"),[],IntType(),Block([],[Return(FieldAccess(SelfLiteral(),Id("val")))])),MethodDecl(Instance(),Id("setVal"),[VarDecl(Id("val"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("deleteNode"),[],BoolType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("next")),NullLiteral()),Assign(FieldAccess(SelfLiteral(),Id("val")),IntLiteral(0))]))]),ClassDecl(Id("List"),[AttributeDecl(Instance(),VarDecl(Id("head"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("tail"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("size"),IntType(),IntLiteral(0))),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("num"),IntType())],None,Block([VarDecl(Id("ele"),ClassType(Id("Node")))],[Assign(FieldAccess(SelfLiteral(),Id("head")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("tail")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("+",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1))),Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("head")),Id("val")),Id("num")),Return(FieldAccess(SelfLiteral(),Id("head")))])),MethodDecl(Instance(),Id("append"),[VarDecl(Id("num"),IntType())],VoidType(),Block([VarDecl(Id("ele"),ClassType(Id("Node")),NewExpr(Id("Node"),[Id("num")]))],[Assign(FieldAccess(FieldAccess(SelfLiteral(),Id("tail")),Id("next")),Id("ele")),Assign(FieldAccess(SelfLiteral(),Id("tail")),FieldAccess(FieldAccess(SelfLiteral(),Id("tail")),Id("next"))),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("+",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1)))])),MethodDecl(Instance(),Id("pop"),[],VoidType(),Block([VarDecl(Id("ptr"),ClassType(Id("Node")),FieldAccess(SelfLiteral(),Id("head")))],[For(Id("i"),IntLiteral(0),FieldAccess(SelfLiteral(),Id("size")),True,Block([],[If(BinaryOp("==",Id("i"),BinaryOp("-",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1))),Block([],[Assign(FieldAccess(Id("ptr"),Id("next")),NullLiteral()),Break()]),Assign(Id("ptr"),FieldAccess(Id("ptr"),Id("next"))))])),CallStmt(FieldAccess(SelfLiteral(),Id("tail")),Id("deleteNode"),[]),Assign(FieldAccess(SelfLiteral(),Id("tail")),Id("ptr")),Assign(FieldAccess(SelfLiteral(),Id("size")),BinaryOp("-",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(1)))])),MethodDecl(Instance(),Id("isEmpty"),[],BoolType(),Block([],[If(BinaryOp("==",FieldAccess(SelfLiteral(),Id("size")),IntLiteral(0)),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),MethodDecl(Instance(),Id("Empty"),[],VoidType(),Block([VarDecl(Id("ptr"),ClassType(Id("Node")),FieldAccess(SelfLiteral(),Id("tail")))],[For(Id("i"),IntLiteral(0),FieldAccess(SelfLiteral(),Id("size")),True,Block([],[Block([],[]),Block([],[])])),Assign(FieldAccess(SelfLiteral(),Id("size")),IntLiteral(0)),Assign(FieldAccess(SelfLiteral(),Id("tail")),NullLiteral()),Assign(FieldAccess(SelfLiteral(),Id("head")),NullLiteral())])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("lis"),ClassType(Id("List")),NewExpr(Id("List"),[IntLiteral(1)])),VarDecl(Id("arr"),ArrayType(100,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7),IntLiteral(8),IntLiteral(9),IntLiteral(19)]))],[For(Id("i"),IntLiteral(0),IntLiteral(100),True,Block([],[CallStmt(Id("lis"),Id("append"),[ArrayCell(Id("arr"),Id("i"))])])),CallStmt(Id("io"),Id("print"),[FieldAccess(Id("lis"),Id("size"))])]))])])
)
        self.assertTrue(TestAST.test(input,expect,377))
    

    def test_78(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        Node(int val){
                            this.val := val;
                        }

                        int getVal(){
                            return this.val;
                        }

                        void setVal(int val){
                            this.val := val;
                        }

                        boolean deleteNode(){
                            this.next := nil;
                            this.val := 0;
                        }

                        void main(){
                            if __name__ == "__main__" then return nil;
                        }
                    }

                
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("val"),IntType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("getVal"),[],IntType(),Block([],[Return(FieldAccess(SelfLiteral(),Id("val")))])),MethodDecl(Instance(),Id("setVal"),[VarDecl(Id("val"),IntType())],VoidType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),Id("val"))])),MethodDecl(Instance(),Id("deleteNode"),[],BoolType(),Block([],[Assign(FieldAccess(SelfLiteral(),Id("next")),NullLiteral()),Assign(FieldAccess(SelfLiteral(),Id("val")),IntLiteral(0))])),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[If(BinaryOp("==",Id("__name__"),StringLiteral("\"__main__\"")),Return(NullLiteral()))]))])])
)
        self.assertTrue(TestAST.test(input,expect,378))
    
    def test_79(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        void main(){
                            if true then{
                                if false then{
                                    if 1 + 2 + 3+ 4 <= 12*2 %23 then{
                                        if t then break;
                                    }
                                }
                                else{
                                    if 1 == 2 then{
                                        if e == true then{

                                        }
                                        else{
                                            if true then break;
                                        }
                                    }
                                    else{continue;}
                                }
                            }
                        }
                    }

                
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([],[If(BooleanLiteral(True),Block([],[If(BooleanLiteral(False),Block([],[If(BinaryOp("<=",BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),BinaryOp("%",BinaryOp("*",IntLiteral(12),IntLiteral(2)),IntLiteral(23))),Block([],[If(Id("t"),Break())]))]),Block([],[If(BinaryOp("==",IntLiteral(1),IntLiteral(2)),Block([],[If(BinaryOp("==",Id("e"),BooleanLiteral(True)),Block([],[]),Block([],[If(BooleanLiteral(True),Break())]))]),Block([],[Continue()]))]))]))]))])])
)
        self.assertTrue(TestAST.test(input,expect,379))

    def test_80(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        void main(){
                            Node a;
                            Node b;
                            a.val := {1,2,3,3.12,"hello", true, false};
                            b.val := a.val;
                            b.next := nil;
                            return b; 
                        }
                    }

                
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ClassType(Id("Node"))),VarDecl(Id("b"),ClassType(Id("Node")))],[Assign(FieldAccess(Id("a"),Id("val")),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),FloatLiteral(3.12),StringLiteral("\"hello\""),BooleanLiteral(True),BooleanLiteral(False)])),Assign(FieldAccess(Id("b"),Id("val")),FieldAccess(Id("a"),Id("val"))),Assign(FieldAccess(Id("b"),Id("next")),NullLiteral()),Return(Id("b"))]))])])
)
        self.assertTrue(TestAST.test(input,expect,380))
    
    def test_81(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        void main(){
                            Node a;
                            Node b;
                            a.val := {1,2,3,3.12,"hello", true, false};
                            b.val := a.val;
                            b.next := nil;
                            b.val[2]  := a.val[1] * 2 / 10 ^("strig" ^ "None") && true || false + (x - !new Node().val);
                            return b; 
                        }
                    }

                
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ClassType(Id("Node"))),VarDecl(Id("b"),ClassType(Id("Node")))],[Assign(FieldAccess(Id("a"),Id("val")),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),FloatLiteral(3.12),StringLiteral("\"hello\""),BooleanLiteral(True),BooleanLiteral(False)])),Assign(FieldAccess(Id("b"),Id("val")),FieldAccess(Id("a"),Id("val"))),Assign(FieldAccess(Id("b"),Id("next")),NullLiteral()),Assign(ArrayCell(FieldAccess(Id("b"),Id("val")),IntLiteral(2)),BinaryOp("||",BinaryOp("&&",BinaryOp("/",BinaryOp("*",ArrayCell(FieldAccess(Id("a"),Id("val")),IntLiteral(1)),IntLiteral(2)),BinaryOp("^",IntLiteral(10),BinaryOp("^",StringLiteral("\"strig\""),StringLiteral("\"None\"")))),BooleanLiteral(True)),BinaryOp("+",BooleanLiteral(False),BinaryOp("-",Id("x"),UnaryOp("!",FieldAccess(NewExpr(Id("Node"),[]),Id("val"))))))),Return(Id("b"))]))])])
)
        self.assertTrue(TestAST.test(input,expect,381))
    
    def test_82(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        void main(){
                            Node a;
                            Node b;
                            a.val := {1,2,3,3.12,"hello", true, false};
                            b.val := a.val;
                            b.next := nil;
                            {
                                final Node a,b = new Node().next,c;
                                if c.val >= 0 then{
                                    a := 1;
                                }
                                else a:=3;
                            }
                            return b; 
                        }
                    }

                
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ClassType(Id("Node"))),VarDecl(Id("b"),ClassType(Id("Node")))],[Assign(FieldAccess(Id("a"),Id("val")),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),FloatLiteral(3.12),StringLiteral("\"hello\""),BooleanLiteral(True),BooleanLiteral(False)])),Assign(FieldAccess(Id("b"),Id("val")),FieldAccess(Id("a"),Id("val"))),Assign(FieldAccess(Id("b"),Id("next")),NullLiteral()),Block([ConstDecl(Id("a"),ClassType(Id("Node")),None),ConstDecl(Id("b"),ClassType(Id("Node")),FieldAccess(NewExpr(Id("Node"),[]),Id("next"))),ConstDecl(Id("c"),ClassType(Id("Node")),None)],[If(BinaryOp(">=",FieldAccess(Id("c"),Id("val")),IntLiteral(0)),Block([],[Assign(Id("a"),IntLiteral(1))]),Assign(Id("a"),IntLiteral(3)))]),Return(Id("b"))]))])])
)
        self.assertTrue(TestAST.test(input,expect,382))
    
    def test_83(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        
                        void main(){
                            Node a;
                            Node b;
                            for i:= 0 to a.size() do{
                                if a.val[i] >= 0 && a.val[i] % 2 == 0 then{
                                    b.val[i] := a.val[i];
                                }
                                else continue;
                            }
                        }
                    }

                
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ClassType(Id("Node"))),VarDecl(Id("b"),ClassType(Id("Node")))],[For(Id("i"),IntLiteral(0),CallExpr(Id("a"),Id("size"),[]),True,Block([],[If(BinaryOp(">=",ArrayCell(FieldAccess(Id("a"),Id("val")),Id("i")),BinaryOp("==",BinaryOp("&&",IntLiteral(0),BinaryOp("%",ArrayCell(FieldAccess(Id("a"),Id("val")),Id("i")),IntLiteral(2))),IntLiteral(0))),Block([],[Assign(ArrayCell(FieldAccess(Id("b"),Id("val")),Id("i")),ArrayCell(FieldAccess(Id("a"),Id("val")),Id("i")))]),Continue())]))]))])])
)
        self.assertTrue(TestAST.test(input,expect,383))
    
    def test_84(self):
        """Simple program: class main {} """
        input = """class Node{
                        int val = 0;
                        Node next = nil;
                        void main(){
                            Node a;
                            int[100] b = {1,2,3,4,5};
                            for i:=0 to 100 do{
                                if i % 2 == 0 || this.isPrime(i) then{
                                    return nil;
                                }
                                continue;
                            }
                        }
                    }

                
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("val"),IntType(),IntLiteral(0))),AttributeDecl(Instance(),VarDecl(Id("next"),ClassType(Id("Node")),NullLiteral())),MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("a"),ClassType(Id("Node"))),VarDecl(Id("b"),ArrayType(100,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))],[For(Id("i"),IntLiteral(0),IntLiteral(100),True,Block([],[If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),BinaryOp("||",IntLiteral(0),CallExpr(SelfLiteral(),Id("isPrime"),[Id("i")]))),Block([],[Return(NullLiteral())])),Continue()]))]))])])
)
        self.assertTrue(TestAST.test(input,expect,384))
    
    def test_85(self):
        """Simple program: class main {} """
        input = """class Node{
                        void func(){
                            return 1;
                        }
                        int foo(int a,b; float c,d; string e,f; boolean g,h){
                            return a*b + (c - d) >= e ^ (f && (g || h));
                        }
                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[MethodDecl(Instance(),Id("func"),[],VoidType(),Block([],[Return(IntLiteral(1))])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType()),VarDecl(Id("e"),StringType()),VarDecl(Id("f"),StringType()),VarDecl(Id("g"),BoolType()),VarDecl(Id("h"),BoolType())],IntType(),Block([],[Return(BinaryOp(">=",BinaryOp("+",BinaryOp("*",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp("^",Id("e"),BinaryOp("&&",Id("f"),BinaryOp("||",Id("g"),Id("h"))))))]))])])
)
        self.assertTrue(TestAST.test(input,expect,385))
    
    def test_86(self):
        """Simple program: class main {} """
        input = """class Node{
                        final static int num = 0;
                        void func(){
                            return 1;
                        }
                        int foo(int a,b; float c,d; string e,f; boolean g,h){
                            return a*b + (c - d) >= e ^ (f && (g || h));
                        }

                        Node(){
                            this.val := num + 1;
                            {
                                this.val := num - a.a.a.a.a[1]; 
                            }
                        }

                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Static(),ConstDecl(Id("num"),IntType(),IntLiteral(0))),MethodDecl(Instance(),Id("func"),[],VoidType(),Block([],[Return(IntLiteral(1))])),MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType()),VarDecl(Id("d"),FloatType()),VarDecl(Id("e"),StringType()),VarDecl(Id("f"),StringType()),VarDecl(Id("g"),BoolType()),VarDecl(Id("h"),BoolType())],IntType(),Block([],[Return(BinaryOp(">=",BinaryOp("+",BinaryOp("*",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp("^",Id("e"),BinaryOp("&&",Id("f"),BinaryOp("||",Id("g"),Id("h"))))))])),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),BinaryOp("+",Id("num"),IntLiteral(1))),Block([],[Assign(FieldAccess(SelfLiteral(),Id("val")),BinaryOp("-",Id("num"),ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("a"),Id("a")),Id("a")),Id("a")),Id("a")),IntLiteral(1))))])]))])])
)
        self.assertTrue(TestAST.test(input,expect,386))
    
    def test_87(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        void abcNode(){

                        }
                        boolean check(int a){
                            if a < 0 then return false;
                            else if a <= 0 then return true;
                            else return nil;
                        }
                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[MethodDecl(Instance(),Id("abcNode"),[],VoidType(),Block([],[])),MethodDecl(Instance(),Id("check"),[VarDecl(Id("a"),IntType())],BoolType(),Block([],[If(BinaryOp("<",Id("a"),IntLiteral(0)),Return(BooleanLiteral(False)),If(BinaryOp("<=",Id("a"),IntLiteral(0)),Return(BooleanLiteral(True)),Return(NullLiteral())))]))],Id("abc"))])
)
        self.assertTrue(TestAST.test(input,expect,387))
    
    def test_88(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        void abcNode(){

                        }
                        boolean check(int a){
                            if a < 0 then return false;
                            else if a <= 0 then return true;
                            else return nil;
                        }
                    }

                   
                    
                """
        expect = str(     
Program([ClassDecl(Id("Node"),[MethodDecl(Instance(),Id("abcNode"),[],VoidType(),Block([],[])),MethodDecl(Instance(),Id("check"),[VarDecl(Id("a"),IntType())],BoolType(),Block([],[If(BinaryOp("<",Id("a"),IntLiteral(0)),Return(BooleanLiteral(False)),If(BinaryOp("<=",Id("a"),IntLiteral(0)),Return(BooleanLiteral(True)),Return(NullLiteral())))]))],Id("abc"))]) 
)
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test_89(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        final static abc abc;
                        static final Final aac;
                    }

                    class n8o extends Node{
                        Node head;
                        Node tail;
                        static int num = 0;
                        n8o(){
                             for abc := 0 downto -1000 do{return 1; break; continue;}

                        }
                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Static(),ConstDecl(Id("abc"),ClassType(Id("abc")),None)),AttributeDecl(Static(),ConstDecl(Id("aac"),ClassType(Id("Final")),None))],Id("abc")),ClassDecl(Id("n8o"),[AttributeDecl(Instance(),VarDecl(Id("head"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("tail"),ClassType(Id("Node")))),AttributeDecl(Static(),VarDecl(Id("num"),IntType(),IntLiteral(0))),MethodDecl(Instance(),Id("<init>"),[],None,Block([],[For(Id("abc"),IntLiteral(0),UnaryOp("-",IntLiteral(1000)),False,Block([],[Return(IntLiteral(1)),Break(),Continue()]))]))],Id("Node"))])
)
        self.assertTrue(TestAST.test(input,expect,389))

    def test_90(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        final static abc abc;
                        static final Final aac;

                        static int increase(abc abc){
                            if abc == 0 then{
                                #this.abc := this.abc[this.abc() + this.abc[12] && true * !false];
                            }
                            return 0;
                        }
                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Static(),ConstDecl(Id("abc"),ClassType(Id("abc")),None)),AttributeDecl(Static(),ConstDecl(Id("aac"),ClassType(Id("Final")),None)),MethodDecl(Static(),Id("increase"),[VarDecl(Id("abc"),ClassType(Id("abc")))],IntType(),Block([],[If(BinaryOp("==",Id("abc"),IntLiteral(0)),Block([],[])),Return(IntLiteral(0))]))],Id("abc"))])
)
        self.assertTrue(TestAST.test(input,expect,390))

    def test_91(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        final static abc abc;
                        static final Final aac;

                        static int increase(abc abc){
                            if abc == 0 then{
                                this.abc := this.abc[this.abc() + this.abc[12] && true * !false];
                            }
                            return 0;
                        }
                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Static(),ConstDecl(Id("abc"),ClassType(Id("abc")),None)),AttributeDecl(Static(),ConstDecl(Id("aac"),ClassType(Id("Final")),None)),MethodDecl(Static(),Id("increase"),[VarDecl(Id("abc"),ClassType(Id("abc")))],IntType(),Block([],[If(BinaryOp("==",Id("abc"),IntLiteral(0)),Block([],[Assign(FieldAccess(SelfLiteral(),Id("abc")),ArrayCell(FieldAccess(SelfLiteral(),Id("abc")),BinaryOp("&&",BinaryOp("+",CallExpr(SelfLiteral(),Id("abc"),[]),ArrayCell(FieldAccess(SelfLiteral(),Id("abc")),IntLiteral(12))),BinaryOp("*",BooleanLiteral(True),UnaryOp("!",BooleanLiteral(False))))))])),Return(IntLiteral(0))]))],Id("abc"))])
)
        self.assertTrue(TestAST.test(input,expect,391))
    

    def test_92(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        final int a;
                        final int b=3e2,c;
                        /*
                            this is a block of comments with \n\f\t
                        */
                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),None)),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),FloatLiteral(300.0))),AttributeDecl(Instance(),ConstDecl(Id("c"),IntType(),None))],Id("abc"))])
)
        self.assertTrue(TestAST.test(input,expect,392))

    
    def test_93(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        final int a;
                        final int b=3e2,c;
                        /*
                            this is a block of comments with \n\f\t
                        */
                        static int foo(float a){
                            if a == this.a then {
                                io.print(io.print(io.print(io.print() ^ io.print(io.print()))));
                            }
                        }
                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),None)),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),FloatLiteral(300.0))),AttributeDecl(Instance(),ConstDecl(Id("c"),IntType(),None)),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),FloatType())],IntType(),Block([],[If(BinaryOp("==",Id("a"),FieldAccess(SelfLiteral(),Id("a"))),Block([],[CallStmt(Id("io"),Id("print"),[CallExpr(Id("io"),Id("print"),[CallExpr(Id("io"),Id("print"),[BinaryOp("^",CallExpr(Id("io"),Id("print"),[]),CallExpr(Id("io"),Id("print"),[CallExpr(Id("io"),Id("print"),[])]))])])])]))]))],Id("abc"))])
)
        self.assertTrue(TestAST.test(input,expect,393))

    
    def test_94(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        final int a;
                        final int b=3e2,c;
                        /*
                            this is a block of comments with \n\f\t
                        */
                        static int foo(float a){
                            int c,d=12,e;
                            if a == this.a then {
                                io.print(io.print(io.print(io.print() ^ io.print(io.print()))));
                            }
                            for a := this.a() downto this.b do{break;break;break;continue;
                            }

                        }

                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),None)),AttributeDecl(Instance(),ConstDecl(Id("b"),IntType(),FloatLiteral(300.0))),AttributeDecl(Instance(),ConstDecl(Id("c"),IntType(),None)),MethodDecl(Static(),Id("foo"),[VarDecl(Id("a"),FloatType())],IntType(),Block([VarDecl(Id("c"),IntType()),VarDecl(Id("d"),IntType(),IntLiteral(12)),VarDecl(Id("e"),IntType())],[If(BinaryOp("==",Id("a"),FieldAccess(SelfLiteral(),Id("a"))),Block([],[CallStmt(Id("io"),Id("print"),[CallExpr(Id("io"),Id("print"),[CallExpr(Id("io"),Id("print"),[BinaryOp("^",CallExpr(Id("io"),Id("print"),[]),CallExpr(Id("io"),Id("print"),[CallExpr(Id("io"),Id("print"),[])]))])])])])),For(Id("a"),CallExpr(SelfLiteral(),Id("a"),[]),FieldAccess(SelfLiteral(),Id("b")),False,Block([],[Break(),Break(),Break(),Continue()]))]))],Id("abc"))])
)
        self.assertTrue(TestAST.test(input,expect,394))

    def test_95(self):
        """Simple program: class main {} """
        input = """class Node extends abc{
                        Node a; Node _b_;
                        int foo(){
                            return this.a.a.a.a(this.b[this.b[this.c.c.a[this.a(12)]]]);
                        }

                    }
                    
                """
        expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("Node")))),AttributeDecl(Instance(),VarDecl(Id("_b_"),ClassType(Id("Node")))),MethodDecl(Instance(),Id("foo"),[],IntType(),Block([],[Return(CallExpr(FieldAccess(FieldAccess(FieldAccess(SelfLiteral(),Id("a")),Id("a")),Id("a")),Id("a"),[ArrayCell(FieldAccess(SelfLiteral(),Id("b")),ArrayCell(FieldAccess(SelfLiteral(),Id("b")),ArrayCell(FieldAccess(FieldAccess(FieldAccess(SelfLiteral(),Id("c")),Id("c")),Id("a")),CallExpr(SelfLiteral(),Id("a"),[IntLiteral(12)]))))]))]))],Id("abc"))])
)
        self.assertTrue(TestAST.test(input,expect,395))
    
    def test_96(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 extends a____b {
                    void main(){
                        Shape s;
                        s.length := true * (false || 12) <= this.abs(-12 + --------100000 % "str" ^ "12"); 
                    }
                }
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Rectangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))]))],Id("Shape")),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape")),ClassDecl(Id("Example2"),[MethodDecl(Static(),Id("main"),[],VoidType(),Block([VarDecl(Id("s"),ClassType(Id("Shape")))],[Assign(FieldAccess(Id("s"),Id("length")),BinaryOp("<=",BinaryOp("*",BooleanLiteral(True),BinaryOp("||",BooleanLiteral(False),IntLiteral(12))),CallExpr(SelfLiteral(),Id("abs"),[BinaryOp("+",UnaryOp("-",IntLiteral(12)),BinaryOp("%",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(100000))))))))),BinaryOp("^",StringLiteral("\"str\""),StringLiteral("\"12\""))))])))]))],Id("a____b"))])
        )
        self.assertTrue(TestAST.test(input,expect,396))
    
    def test_97(self):
        """Simple program: class main {} """
        input = """class Shape {
                        float length,width;
                        float getArea() {
                            return this.length() * this.getSrea();
                        }
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                /*class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }*/
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                """
        expect = str(      
Program([ClassDecl(Id("Shape"),[AttributeDecl(Instance(),VarDecl(Id("length"),FloatType())),AttributeDecl(Instance(),VarDecl(Id("width"),FloatType())),MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("*",CallExpr(SelfLiteral(),Id("length"),[]),CallExpr(SelfLiteral(),Id("getSrea"),[])))])),MethodDecl(Instance(),Id("<init>"),[VarDecl(Id("length"),FloatType()),VarDecl(Id("width"),FloatType())],None,Block([],[Assign(FieldAccess(SelfLiteral(),Id("length")),Id("length")),Assign(FieldAccess(SelfLiteral(),Id("width")),Id("width"))]))]),ClassDecl(Id("Triangle"),[MethodDecl(Instance(),Id("getArea"),[],FloatType(),Block([],[Return(BinaryOp("/",BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))),IntLiteral(2)))]))],Id("Shape"))])
        )
        self.assertTrue(TestAST.test(input,expect,397))
    
    

    def test_98(self):
            """Simple program: class main {} """
            input = """class Node extends abc{
                            Node a;
                            void foo(){
                                return new Node(1,2,3,4, {1,2,3,4} , Node, boolan).Boolean(true,false);
                            }
                        }
                        
                    """
            expect = str(      
Program([ClassDecl(Id("Node"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("Node")))),MethodDecl(Instance(),Id("foo"),[],VoidType(),Block([],[Return(CallExpr(NewExpr(Id("Node"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),Id("Node"),Id("boolan")]),Id("Boolean"),[BooleanLiteral(True),BooleanLiteral(False)]))]))],Id("abc"))])
    )
            self.assertTrue(TestAST.test(input,expect,398))
    

    def test_99(self):
            """Simple program: class main {} """
            input = """class A{
                            
                        }

                        class B extends A{

                        }

                        class C extends B{

                        }

                        class D extends extend{
                            A a;
                            B b;
                            C c,d;
                            void printTheEnd(string ppl){
                                    io.cout("This is the end of Assignment2 " ^ ppl);
                                    return nil;
                            }
                        }
                        
                    """
            expect = str(      
Program([ClassDecl(Id("A"),[]),ClassDecl(Id("B"),[],Id("A")),ClassDecl(Id("C"),[],Id("B")),ClassDecl(Id("D"),[AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("A")))),AttributeDecl(Instance(),VarDecl(Id("b"),ClassType(Id("B")))),AttributeDecl(Instance(),VarDecl(Id("c"),ClassType(Id("C")))),AttributeDecl(Instance(),VarDecl(Id("d"),ClassType(Id("C")))),MethodDecl(Instance(),Id("printTheEnd"),[VarDecl(Id("ppl"),StringType())],VoidType(),Block([],[CallStmt(Id("io"),Id("cout"),[BinaryOp("^",StringLiteral("\"This is the end of Assignment2 \""),Id("ppl"))]),Return(NullLiteral())]))],Id("extend"))])
    )
            self.assertTrue(TestAST.test(input,expect,399))
    
    

