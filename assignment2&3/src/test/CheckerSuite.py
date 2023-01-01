import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):

        def test_0(self):
            input ="""
    class A{

    }
    class A{

    }
    """
            expect = "Redeclared Class: A"
            self.assertTrue(TestChecker.test(input, expect, 400))
        

        def test_1(self):
            input ="""
    class A{
        int a;
        int a;
        void main(){}
    }
    """
            expect = "Redeclared Attribute: a"
            self.assertTrue(TestChecker.test(input, expect, 401))

        
        def test_2(self):
            input ="""
    class A{
        int a;
        float a;
        void main(){}
    }
    """
            expect = "Redeclared Attribute: a"
            self.assertTrue(TestChecker.test(input, expect, 402))

        def test_3(self):
            input ="""
    class A{
        int a;
        int a(){

        }
        void main(){}
    }
    """
            expect = "Redeclared Method: a"
            self.assertTrue(TestChecker.test(input, expect, 403))

        def test_4(self):
            input ="""
    class A{
        int a;
        int b(){
                int a;
                int c;
                float c;
        }
        void main(){}
    }
    """
            expect = "Redeclared Variable: c"
            self.assertTrue(TestChecker.test(input, expect, 404))
        
        def test_5(self):
            input ="""
    class A{
        int a;
        int b(){
                int a;
                int c;
                if a >= 0 then{
                        int a;
                        float c;
                        string d;
                        boolean d;
                }
                
        }
        void main(){}
    }
    """
            expect = "Redeclared Variable: d"
            self.assertTrue(TestChecker.test(input, expect, 405))
        
        def test_6(self):
            input ="""
    class A{
        int a;
        int b(){
                int a;
                int c;
                if a >= 0 then{
                        int a;
                        float c;
                        string d;
                        {
                                int c;
                                int d;
                                {
                                        float c;
                                        boolean d;
                                }

                                {
                                        int c,d;
                                        final float a = 1,d =1;
                                }
                        }
                        
                }
                
        }
        void main(){}
    }
    """
            expect = "Redeclared Constant: d"
            self.assertTrue(TestChecker.test(input, expect, 406))
        
        def test_7(self):
            input ="""
    class A{
        int a;
        int b(){
                int a;
                int c;
                int b;

        }
        static float b(){}
        void main(){}
    }
    """
            expect = "Redeclared Method: b"
            self.assertTrue(TestChecker.test(input, expect, 407))
        

        def test_8(self):
            input ="""
    class A{
        int a;
        int b(string b, d,e; int as){
                int a;
                int c;
                final int b;
                return b + 1;
        }
        void main(){}
    }
    """
            expect = "Redeclared Constant: b"
            self.assertTrue(TestChecker.test(input, expect, 408))

        def test_9(self):
            input ="""
    class A{
        int a;
        int b(string b, d,e; int as; float b){
                
        }
        void main(){}
    }
    """
            expect = "Redeclared Parameter: b"
            self.assertTrue(TestChecker.test(input, expect, 409)) 
        

        def test_10(self):
            input ="""
    class A{
        int a;
        int b(string b, d,e; int as){
                f:= as + 1;
        }
        void main(){}
    }
    """
            expect = "Undeclared Identifier: f"
            self.assertTrue(TestChecker.test(input, expect, 410))
        
        def test_11(self):
            input ="""
    class A{
        int a;
        int b(string b, d,e; int as){
                A a;
                A a;
        }
        void main(){}
    }
    """
            expect = "Redeclared Variable: a"
            self.assertTrue(TestChecker.test(input, expect, 411))
        
        def test_12(self):
            input ="""
    class A{
        int a;
        int b(){
                int a;
                int c;
                if a >= 0 then{
                        int a;
                        float c;
                        string d;
                        {
                                int c;
                                int d;
                                {
                                        float c;
                                        boolean d;
                                }

                                {
                                        c:= c+1;
                                        e:= 3 * 4;
                                }
                        }
                        
                }
                
        }
        void main(){}
    }
    """
            expect = "Undeclared Identifier: e"
            self.assertTrue(TestChecker.test(input, expect, 412))

        def test_13(self):
            input ="""
    class A{
        final int a;
        int b(string b, d,e; int as){
            
        }
        void main(){}
    }
    """
            expect = "Illegal Constant Expression: None"
            self.assertTrue(TestChecker.test(input, expect, 413))
        
        def test_14(self):
            input ="""
    class A{
        final int a;
        int b(string b, d,e; int as){
            
        }
        void main(){}
    }
    """
            expect = "Illegal Constant Expression: None"
            self.assertTrue(TestChecker.test(input, expect, 414))
        
        def test_15(self):
            input ="""
    class A{
        final int a = 1;
        int b(string b, d,e; int as){
            int a = 2;
            final float c;
        }
        void main(){}
    }
    """
            expect = "Illegal Constant Expression: None"
            self.assertTrue(TestChecker.test(input, expect, 415))
        

        def test_16(self):
            input ="""
    class A{
        final int a = 1;
        int b(string b, d,e; int as){
            z := as + 2;
        }
        void main(){}
    }
    """
            expect = "Undeclared Identifier: z"
            self.assertTrue(TestChecker.test(input, expect, 416))
        
        def test_17(self):
            input ="""
    class A{
        final int a = 1;
        int b(string b, d,e; int as){
            as := as + 2 + de;
        }
        void main(){}
    }
    """
            expect = "Undeclared Identifier: de"
            self.assertTrue(TestChecker.test(input, expect, 417))
        
        def test_18(self):
            input ="""
    class A{
        final int a = 1;
        int b(string b, d,e; int as){
            return 1.2;
        }
    }
    """
            expect = "Type Mismatch In Statement: Return(FloatLit(1.2))"
            self.assertTrue(TestChecker.test(input, expect, 418))
        
        def test_19(self):
            input ="""
    class A{
        final int a = 1;
        int b(string b, d,e; int as){
        }
        void main(){
            this.a := 1 * 2;
        }
    }
    """
            expect = """Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(*,IntLit(1),IntLit(2)))"""
            self.assertTrue(TestChecker.test(input, expect, 419))
        

        def test_20(self):
            input ="""
    class A{
        final int a = 1;
        int c;
        int b(string b, d,e; int as){
        }
        void main(){
            this.c := 1 * this.b;
        }
    }
    """
            expect = """Undeclared Attribute: b"""
            self.assertTrue(TestChecker.test(input, expect, 420))
        
        def test_21(self):
            input ="""
    class A{
        final int a = 1;
        int c;
        void main(){
            this.c := 1 * this.bc;

        }
        int bc;
        Bd aa;
    }
    """
            expect = """Undeclared Class: Bd"""
            self.assertTrue(TestChecker.test(input, expect, 421))
        
        def test_22(self):
            input ="""
    class A{
        final int a = 1;
        boolean c;
        void main(){
            this.c := 1 * this.bc;

        }
        int bc;
    }
    """
            expect = """Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(c)),BinaryOp(*,IntLit(1),FieldAccess(Self(),Id(bc))))"""
            self.assertTrue(TestChecker.test(input, expect, 422))
        
        def test_23(self):
            input ="""
    class A{
        final int a = 1;
        float c;
        void main(){
            this.c := 1 * this.bc;

        }
        int bc;
        Bb aa = 2.3;
    }
    class Bb{

    }
    """
            expect = """Type Mismatch In Statement: VarDecl(Id(aa),ClassType(Id(Bb)),FloatLit(2.3))"""
            self.assertTrue(TestChecker.test(input, expect, 423))
        
        def test_24(self):
            input ="""
    class A{
        final int a = 1;
        float c;
        void method(){

        }
        void main(){
            this.c := 1 * this.bc;
            this.methoda();
        }
        int bc;
    }
    class Bb{

    }
    """
            expect = """Undeclared Method: methoda"""
            self.assertTrue(TestChecker.test(input, expect, 424))
        
        def test_25(self):
            input ="""
    class A{
        final int a = 1;
        float c;
        string method(){

        }
        void main(){
            this.c := 1 * this.bc;
            this.method();
        }
        int bc;
    }
    class Bb{

    }
    """
            expect = """Type Mismatch In Statement: Call(Self(),Id(method),[])"""
            self.assertTrue(TestChecker.test(input, expect, 425))
        
        def test_26(self):
            input ="""
    class A{
        final int a = 1;
        float c;
        void method(){

        }
        void main(){
            this.c := 1 * this.bc;
            this.method(1);
        }
        int bc;
    }
    class Bb{

    }
    """
            expect = """Type Mismatch In Statement: Call(Self(),Id(method),[IntLit(1)])"""
            self.assertTrue(TestChecker.test(input, expect, 426))
        
        def test_27(self):
            input ="""
    class A{
        final int a = 1;
        float c;
        void method(){

        }
        void main(){
            this.c := 1 * this.bc;
            #this.method(1);
        }
        static int bc;
    }
    class Bb{

    }
    """
            expect = """Illegal Member Access: FieldAccess(Self(),Id(bc))"""
            self.assertTrue(TestChecker.test(input, expect, 427))
        
       

        def test_28(self):
            input ="""
    class A{
        final int a = 1;
        float c;
        void method(){

        }
        void main(){
            A va;
            this.c := 1 * A.bc;
            this.c := 1 * va.bc;
        }
        static int bc = 1;
    }
    class Bb{

    }
    """
            expect = """Illegal Member Access: FieldAccess(Id(va),Id(bc))"""
            self.assertTrue(TestChecker.test(input, expect, 428))

        def test_29(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            A va = new A(12);
            this.c := 1 * A.bc;
        }
        static int bc = 1;
    }
    class Bb{

    }
    """
            expect = """Undeclared Method: <init>"""
            self.assertTrue(TestChecker.test(input, expect, 429))

        def test_30(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){
            return 1;
        }
        void main(){
            A va;
            this.c := 1 * A.bc;
        }
        static int bc = 1;
    }
    class Bb{

    }
    """
            expect = """Type Mismatch In Statement: Return(IntLit(1))"""
            self.assertTrue(TestChecker.test(input, expect, 430))

        def test_31(self):#o day
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            A va;
            this.c := 1 * A.bc;
        }
        static int bc = 1;
    }
    class Bb extends pp{

    }
    """
            expect = """Undeclared Class: pp"""
            self.assertTrue(TestChecker.test(input, expect, 431))

        def test_32(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            A va;
            this.c := 1 * A.bc;
        }
        static int bc = 1;
    }
    class Bb extends A{
        int a = 2;
        void foo(){
            io.readint();

        }
    }
    """
            expect = """Undeclared Method: readint"""
            self.assertTrue(TestChecker.test(input, expect, 432))

        def test_33(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            A va;
            this.c := 1 * A.bc;
        }
        static int bc = 1;
    }
    class Bb extends A{
        void foo(){
            io.writeInt(25);
            this.a := 2;
            b := 1 + 2;
        }
    }
    """
            expect = """Undeclared Identifier: b"""
            self.assertTrue(TestChecker.test(input, expect, 433))
        
        def test_34(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            A va;
            this.c := 1 * A.bc;
        }
        static int bc = 1;
    }
    class Bb {
        void foo(){
            io.writeInt(25);
            this.a := 2;
        }
    }
    """
            expect = """Undeclared Attribute: a"""
            self.assertTrue(TestChecker.test(input, expect, 434))
        
        def test_35(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            A va;
            this.c := 1 * A.bc;
        }
        static int bc = 1;
    }
    class Bb {
        void foo(){
            io.readInt(25);
        }
    }
    """
            expect = """Type Mismatch In Statement: Call(Id(io),Id(readInt),[IntLit(25)])"""
            self.assertTrue(TestChecker.test(input, expect, 435))
        
        def test_36(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            final boolean var = 12;
        }
        static int bc = 1;
    }
    class Bb {
        void foo(){
            
        }
    }
    """
            expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(var),BoolType,IntLit(12))"""
            self.assertTrue(TestChecker.test(input, expect, 436))
        
        def test_37(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            string a = "hello";
            final string var = a;
        }
        static int bc = 1;
    }
    class Bb {
        void foo(){
            
        }
    }
    """
            expect = """Illegal Constant Expression: Id(a)"""
            self.assertTrue(TestChecker.test(input, expect, 437))
        
        def test_38(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            final float b = 12;
            int c = 1;
            final float var = 12 + b * c;
        }
        static int bc = 1;
    }
    
    """
            expect = """Illegal Constant Expression: BinaryOp(+,IntLit(12),BinaryOp(*,Id(b),Id(c)))"""
            self.assertTrue(TestChecker.test(input, expect, 438))

        def test_39(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            int[3] arr;
            arr := {1,2,3,4};
        }
        static int bc = 1;
    }
    
    """
            expect = """Type Mismatch In Statement: AssignStmt(Id(arr),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])"""
            self.assertTrue(TestChecker.test(input, expect, 439))

        def test_40(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            int[3] arr = {1,2,3.3};
        }
        static int bc = 1;
    }
    
    """
            expect = """Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3.3)]"""
            self.assertTrue(TestChecker.test(input, expect, 440))

        
        def test_41(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            int[3] arr = {1,2,3};
            final int[3] arrr = arr;
        }
        static int bc = 1;
    }
    
    """
            expect = """Illegal Constant Expression: Id(arr)"""
            self.assertTrue(TestChecker.test(input, expect, 441))

        def test_42(self):
            input ="""
    class A{
        int a = 1;
        float c;
        A(){

        }
        void main(){
            int[3] arr = {1,2,3};
        }
        static int bc = 1;
    }
    class B extends A{
        void foo(){
            this.main(1);
            this.foo();
            this.func();   
        }
    }
    """
            expect = """Illegal Member Access: Call(Self(),Id(main),[IntLit(1)])"""
            self.assertTrue(TestChecker.test(input, expect, 442))

        def test_43(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            int[3] arr = {1,2,3};
        }
    }
    class B extends A{
        void foo(){
            A.main();
            this.foo();
            this.func();   
        }
    }
    """
            expect = """Undeclared Method: func"""
            self.assertTrue(TestChecker.test(input, expect, 443))
        
        def test_44(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            int[3] arr = {1,2,3};
        }
    }
    class B extends A{
        void foo(){
            A.main(1,2,3);
            this.foo();
        }
    }
    """
            expect = """Type Mismatch In Statement: Call(Id(A),Id(main),[IntLit(1),IntLit(2),IntLit(3)])"""
            self.assertTrue(TestChecker.test(input, expect, 444))

        def test_45(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            final int[3] arr = {1,2,true};
        }
    }
    """
            expect = """Illegal Array Literal: [IntLit(1),IntLit(2),BooleanLit(True)]"""
            self.assertTrue(TestChecker.test(input, expect, 445))
        
        def test_46(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            
        }
    }
    class B extends A{
        void foo(){
            B obj_b = nil;
            A obj = obj_b;
            return 1;
        }
            
    }
    """
            expect = """Type Mismatch In Statement: Return(IntLit(1))"""
            self.assertTrue(TestChecker.test(input, expect, 446))
        
        def test_47(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            
        }
    }
    class B extends A{
        void foo(){
            A obj_a = nil;
            B obj;
            obj := obj_a;
        
        }
            
    }
    
    """
            expect = """Type Mismatch In Statement: AssignStmt(Id(obj),Id(obj_a))"""
            self.assertTrue(TestChecker.test(input, expect, 447))

        def test_48(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            
        }
    }
    class B extends A{
        void foo(){
            
        
        }
            
    }
    class C extends B{
        void func(){
            A obj_a = nil;
            B obj_b = nil;
            C obj_c = nil;
            obj_a := obj_c;
            obj_b := obj_c;
            return true;
        }
    }
    """
            expect = """Type Mismatch In Statement: Return(BooleanLit(True))"""
            self.assertTrue(TestChecker.test(input, expect, 448))
        
        def test_49(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            
        }
    }
    class B extends A{
        void foo(){
            
        
        }
            
    }
    class C extends B{
        void func(){
            A obj_a = nil;
            B obj_b = nil;
            C obj_c = nil;
            obj_a := obj_c;
            obj_b := obj_c;
            obj_c := obj_a;
        }
    }
    """
            expect = """Type Mismatch In Statement: AssignStmt(Id(obj_c),Id(obj_a))"""
            self.assertTrue(TestChecker.test(input, expect, 449))

        def test_50(self):
            input ="""
    class A{
        int a = 1;
        float c;
        void main(){
            
        }
    }
    class B extends A{
        void foo(){
            
        
        }
            
    }
    class C extends A{
        void func(){
            A obj_a = nil;
            B obj_b = nil;
            C obj_c = nil;
            obj_a := obj_c;
            obj_b := obj_c;
        }
    }
    """
            expect = """Type Mismatch In Statement: AssignStmt(Id(obj_b),Id(obj_c))"""
            self.assertTrue(TestChecker.test(input, expect, 450))
        
        #x.b[2] := x.m()[3];
        def test_51(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        A(){

        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            A x = new A();
            x.b[2] := x.m()[3];
            return 1;
        }
    }
    
    """
            expect = """Type Mismatch In Statement: Return(IntLit(1))"""
            self.assertTrue(TestChecker.test(input, expect, 451))
        
        def test_52(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        A(){

        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            A x = new A();
            int nu = 3;
            x.b[nu-1] := x.m()[nu];
            return "string";
        }
    }
    
    """
            expect = """Type Mismatch In Statement: """+ str(Return(StringLiteral("\"string\"")))
            self.assertTrue(TestChecker.test(input, expect, 452))

        def test_53(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        A(){

        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            A x = new A();
            int nu = 3;
            x.b[nu-1] := x.m()[nu+0.5];
            return "string";
        }
    }
    
    """
            expect = """Type Mismatch In Expression: ArrayCell(CallExpr(Id(x),Id(m),[]),BinaryOp(+,Id(nu),FloatLit(0.5)))"""
            self.assertTrue(TestChecker.test(input, expect, 453))
        
        def test_54(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        A(){

        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            final int x = 12;
            final float y = 20;
            final float z = x + y;
            return 1;
        }
    }
    
    """
            expect = """Type Mismatch In Statement: Return(IntLit(1))"""
            self.assertTrue(TestChecker.test(input, expect, 454))
        
        def test_55(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        A(){

        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            final int x = 12;
            final float y = 20;
            final float z = x + y;
            final float t = z*x - y + 12 % 10 / 2 * 1;
            return 1;
        }
    }
    
    """
            expect = """Type Mismatch In Statement: Return(IntLit(1))"""
            self.assertTrue(TestChecker.test(input, expect, 455))
        
        def test_56(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        A(){

        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            final int x = 12;
            final float y = 20;
            final float z = x + y;
            final float t = 1.0 || false;
            return 1;
        }
    }
    
    """
            expect = """Type Mismatch In Expression: BinaryOp(||,FloatLit(1.0),BooleanLit(False))"""
            self.assertTrue(TestChecker.test(input, expect, 456))

        def test_57(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
            return b; 
        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            final int x = 12;
            
        }
    }
    
    """
            expect = """Type Mismatch In Statement: Return(Id(b))"""
            self.assertTrue(TestChecker.test(input, expect, 457))
        
        def test_58(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
            this.b[3] := b + this.m();
        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            final int x = 12;
            
        }
    }
    
    """
            expect = """Type Mismatch In Expression: BinaryOp(+,Id(b),CallExpr(Self(),Id(m),[]))"""
            self.assertTrue(TestChecker.test(input, expect, 458))
        

        def test_59(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(){
            this.c := this.c + 0.1;
        }
        int[5] m(){
            int[5] arr = {1,2,3,4,5};
            return arr;
        }
        void main(){
            final int x = 12;
            A obj = new A();
            obj.c := true;
        }
    }
    
    """
            expect = """Type Mismatch In Statement: AssignStmt(FieldAccess(Id(obj),Id(c)),BooleanLit(True))"""
            self.assertTrue(TestChecker.test(input, expect, 459))
        
        def test_60(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; float b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            
        }
        void main(){
            final int x = 12;
            final string str = "string";
            A obj = new A(true, 1, str);
        }
    }
    
    """
            expect = """Type Mismatch In Expression: NewExpr(Id(A),[BooleanLit(True),IntLit(1),Id(str)])"""
            self.assertTrue(TestChecker.test(input, expect, 460))
        
        def test_61(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final string str = "string";
            A obj = this.m();
            obj.c := true;
        }
    }
    
    """
            expect = """Type Mismatch In Statement: AssignStmt(FieldAccess(Id(obj),Id(c)),BooleanLit(True))"""
            self.assertTrue(TestChecker.test(input, expect, 461))

        def test_62(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final string str = "string";
            boolean bo = this.m().a && true || false;
            int aaa;
            aaa:=this.m().c;
        }
    }
    
    """
            expect = """Type Mismatch In Statement: AssignStmt(Id(aaa),FieldAccess(CallExpr(Self(),Id(m),[]),Id(c)))"""
            self.assertTrue(TestChecker.test(input, expect, 462))

        def test_63(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final float y = 11;
            if x == 12 then y := true;
        }
    }
    
    """
            expect = """Cannot Assign To Constant: AssignStmt(Id(y),BooleanLit(True))"""
            self.assertTrue(TestChecker.test(input, expect, 463))

        def test_64(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final float y = 11;
            if (x == 12) || true then y := true; else{}
        }
    }
    
    """
            expect = """Cannot Assign To Constant: AssignStmt(Id(y),BooleanLit(True))"""
            self.assertTrue(TestChecker.test(input, expect, 464))

        def test_65(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final float y = 11;
            if (x == 12) || true then this.a := false; 
            else{
                if x == 12 - 1e-2 then{
                    x := x;
                }
            }
        }
    }
    
    """
            expect = """Type Mismatch In Expression: BinaryOp(==,Id(x),BinaryOp(-,IntLit(12),FloatLit(0.01)))"""
            self.assertTrue(TestChecker.test(input, expect, 465))

        def test_66(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final float y = 11;
            if (x == 12) || true then this.a := false; 
            else{
                if x == 12 + 1 then{
                    if false then {

                    }
                    else{
                        final float z = 1.2;
                        z := io.readFloat();
                    }
                }
                else{

                }
            }
        }
    }
    
    """
            expect = """Cannot Assign To Constant: AssignStmt(Id(z),CallExpr(Id(io),Id(readFloat),[]))"""
            self.assertTrue(TestChecker.test(input, expect, 466))
        
        def test_67(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final float y = 11;
            if (x == 12) || true then this.a := false; 
            else{
                if x == 12 + 1 then{
                    {
                        final float z = 1.2;
                        io.writeFloat(true);
                        {}
                    }
                }
            }
        }
    }
    
    """
            expect = """Type Mismatch In Statement: Call(Id(io),Id(writeFloat),[BooleanLit(True)])"""
            self.assertTrue(TestChecker.test(input, expect, 467))

        def test_68(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final float y = 11;
            if (x == 12) || true then this.a := false; 
            else{
                if x == 12 + 1 then{
                    {
                        final float z = 1.2;
                        io.writeInt(io.readFloat());
                    }
                }
            }
        }
    }
    
    """
            expect = """Type Mismatch In Statement: Call(Id(io),Id(writeInt),[CallExpr(Id(io),Id(readFloat),[])])"""
            self.assertTrue(TestChecker.test(input, expect, 468))
        
        def test_69(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(boolean a; int b; float c){
            this.a := a;
            this.c := c;
        }
        A m(){
            A obj = new A(true,1,2.2);
            return obj;
        }
        void main(){
            final int x = 12;
            final float y = 11;
            if (x == 12) || true then this.a := false; 
            else{
                if x == 12 + 1 then{
                    {
                        final float z = 1.2;
                        io.writeFloat(io.readFloat());
                        break;
                    }
                }
            }
        }
    }
    
    """
            expect = """Break Not In Loop"""
            self.assertTrue(TestChecker.test(input, expect, 469))

        def test_70(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        void mmain(){
            final int x = 12;
            final float y = 11;
            if (x == 12) || true then this.a := false; 
            else{
                if x == 12 + 1 then{
                    {
                        final float z = 1.2;
                        io.writeFloat(io.readFloat());
                    }
                }
            }
        }
    }
    class B extends A{
        void func(){
            this.mmain();
            B.str := B.str ^ "hello";
            B.str := B.str + this.mmain();
        }
        static string str = "function";
    }
    """
            expect = """Type Mismatch In Expression: CallExpr(Self(),Id(mmain),[])"""
            self.assertTrue(TestChecker.test(input, expect, 470))

        
        def test_71(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        void mmain(){
            for i:=1 to 2 do{

            }
        }
    }
    class B extends A{
    }
    """
            expect = """Undeclared Identifier: i"""
            self.assertTrue(TestChecker.test(input, expect, 471))

        def test_72(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        void mmain(){
            final int i = 0;
        }
    }
    class B extends A{
        void foo(A obj; int x, y; float z){

        }

        void fun(){
            A ob = new A();
            B o = new B();
            this.foo(this,2,3,1);
            this.foo(o, 1, 2, 3);
            this.mmain(1);
        }
    }
    """
            expect = """Type Mismatch In Statement: Call(Self(),Id(mmain),[IntLit(1)])"""
            self.assertTrue(TestChecker.test(input, expect, 472))

        def test_73(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        void mmain(){
            int i = 0;
            for i:=1 to 2.2 do{

            }
        }
    }
    class B extends A{

    }
    """
            expect = """Type Mismatch In Statement: For(Id(i),IntLit(1),FloatLit(2.2),True,Block([],[])])"""
            self.assertTrue(TestChecker.test(input, expect, 473))

        def test_74(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        int m(){
            return 1;
        }
        void mmain(){
            int i = 0;
            for i:=1 to this.b[4] + this.m() do{
                if i % 2 == 0 then{
                    break;
                }
                else{
                   
                }
            }
        }
    }
    class B extends A{
        void foo(A obj; int x, y; float z){

        }

        void fun(){
            A ob = new A();
            this.foo(ob,2,3,1);
            this.mmain(1);
        }
    }
    """
            expect = """Type Mismatch In Statement: Call(Self(),Id(mmain),[IntLit(1)])"""
            self.assertTrue(TestChecker.test(input, expect, 474))

        
        def test_75(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        int m(){
            return 1;
        }
        void mmain(){
            int i = 0;
            int j = 1;
            for i:=1 downto this.b[4] + this.m() do{
                for j := 2 to this.b[this.m()] do{
                    break;
                }
                continue;
            }
            continue;
        }
    }
    class B extends A{
    }
    """
            expect = """Continue Not In Loop"""
            self.assertTrue(TestChecker.test(input, expect, 475))

        def test_76(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        int m(){
            return 1;
        }
        void mmain(){
            int i = 0;
            int j = 1;
            for i:=1 downto this.b[4] + this.m() do{
                for j := this.m()*2+this.b[4] to this.b[this.m()] do{
                    break;
                    if true then{break;}
                    return true;
                }
                continue;
            }
        }
    }
    class B extends A{
    }
    """
            expect = """Type Mismatch In Statement: Return(BooleanLit(True))"""
            self.assertTrue(TestChecker.test(input, expect, 476))

        
        def test_77(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        int m(){
            return 1;
        }
        boolean mmain(){
            int i = 0;
            int j = 1;
            int k = 0;
            for i:=1 downto this.b[4] + this.m() do{
                for j := 2 to this.b[this.m()] do{
                    break;
                    if true then{break;}
                    return true;
                }
                for k:= this.b[2] downto 3 do{
                    final boolean truth = true;
                    break;
                    this.b[k] := this.b[k] % 10;
                    return truth * this.b[k*2];
                }
            }
        }
    }
    class B extends A{
    }
    """
            expect = """Type Mismatch In Expression: BinaryOp(*,Id(truth),ArrayCell(FieldAccess(Self(),Id(b)),BinaryOp(*,Id(k),IntLit(2))))"""
            self.assertTrue(TestChecker.test(input, expect, 477))


        def test_78(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        int m(){
            return 1;
        }
        boolean mmain(){
            int i = 0;
            int j = 1;
            int k = 0;
            for i:=1 downto this.b[4] + this.m() do{
                float k;
                for j := 2 to this.b[this.m()] do{
                    break;
                    if true then{break;}
                    return true;
                }
                for k:= this.b[2] downto 3 do{
                    final boolean truth = true;
                    break;

                }
            }
        }
    }
    class B extends A{
    }
    """
            expect = """Type Mismatch In Statement: For(Id(k),ArrayCell(FieldAccess(Self(),Id(b)),IntLit(2)),IntLit(3),False,Block([ConstDecl(Id(truth),BoolType,BooleanLit(True))],[Break])])"""
            self.assertTrue(TestChecker.test(input, expect, 478))

        def test_79(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        int m(){
            return 1;
        }
        boolean mmain(){
            int i = 0;
            int j = 1;
            int k = 0;
            for i:=1 downto this.b[4] + this.m() do{
                float k;
                for j := 2 to this.b[this.m()] do{
                    break;
                    if true then{break;}
                    return true;
                }
                for k:= this.b[2] downto 3 do{
                    final boolean truth = true;
                    break;

                }
            }
        }
    }
    class B extends A{
    }
    """
            expect = """Type Mismatch In Statement: For(Id(k),ArrayCell(FieldAccess(Self(),Id(b)),IntLit(2)),IntLit(3),False,Block([ConstDecl(Id(truth),BoolType,BooleanLit(True))],[Break])])"""
            self.assertTrue(TestChecker.test(input, expect, 479))

        
        def test_80(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        int m(){
            return 1;
        }
        boolean mmain(){
            this.c := this.m() + 1;
            return this.a;
        }
    }
    class B extends A{
        boolean boo = this.a && this.c;
    }
    """
            expect = """Type Mismatch In Expression: BinaryOp(&&,FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(c)))"""
            self.assertTrue(TestChecker.test(input, expect, 480))

        
        def test_81(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(int as; string str){
            this.c := as;
        }
        boolean mmain(){
            #A o = new A();
            return this.a;
        }
    }
    class B extends A{
        A obj = new A(1);
    }
    """
            expect = """Type Mismatch In Expression: NewExpr(Id(A),[IntLit(1)])"""
            self.assertTrue(TestChecker.test(input, expect, 481))

        def test_82(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(int as; string str){
            this.c := as;
        }
        boolean mmain(int o){
            A o = new A(1, "1");
            return this.a;
        }
    }
    class B extends A{
        A obj = new A(1);
    }
    """
            expect = """Redeclared Variable: o"""
            self.assertTrue(TestChecker.test(input, expect, 482))

        def test_83(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(int as; string str){
            this.c := as;
        }
        boolean mmain(){
            #A o = new A();
            continue;
            return this.a;
        }
    }

    """
            expect = """Continue Not In Loop"""
            self.assertTrue(TestChecker.test(input, expect, 483))

        def test_84(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        A(int as; string str){
            this.c := as;
        }
        boolean mmain(int c; string str; float str){
            #continue;
            return this.a;
        }
    }

    """
            expect = """Redeclared Parameter: str"""
            self.assertTrue(TestChecker.test(input, expect, 484))

        def test_85(self):
            input ="""
    class A extends TestChecker{
        float c;
        boolean a;
        A(int as; string str){
            this.c := as;
        }
        boolean mmain(int c){
            #continue;
            return this.a;
        }
    }

    """
            expect = """Undeclared Class: TestChecker"""
            self.assertTrue(TestChecker.test(input, expect, 485))

        def test_86(self):
            input ="""
    class A {
        float c;
        boolean a;
        A(int as; string str){
            this.c := as;
        }
        boolean mmain(int c){
            A o = new A().c;
            #continue;
            return this.a;
        }
    }

    """
            expect = """Type Mismatch In Expression: NewExpr(Id(A),[])"""
            self.assertTrue(TestChecker.test(input, expect, 486))

        def test_87(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; string str){
            
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    class B extends A{
        void foo(){
            B.c := 1;
            return true;
        }
    }
    """
            expect = """Type Mismatch In Statement: Return(BooleanLit(True))"""
            self.assertTrue(TestChecker.test(input, expect, 487))

        def test_88(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; string str){
            
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    class B extends A{
        boolean foo(){
            A.c := 1 ;
            this.a := this.mmain(21) && this.mmain(12);
            return 1;
        }
    }
    """
            expect = """Type Mismatch In Statement: Return(IntLit(1))"""
            self.assertTrue(TestChecker.test(input, expect, 488))

        def test_89(self):
            input ="""
    class A{
        int[5] b = {1,2,3,4,5};
        float c;
        boolean a;
        void mmain(){
            final int i = 0;
        }
    }
    class B extends A{
        void foo(A obj; int x, y; float z){

        }

        int fun(boolean par){
            A ob = new A();
            B o = new B();
            if par then return 1;
            else return this.fun(this.a);
        }
        void f(){
            continue;
        }
    }
    """
            expect = """Continue Not In Loop"""
            self.assertTrue(TestChecker.test(input, expect, 489))


        def test_90(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    class B extends A{
        A foo(){
            final float pi = 3.14;
            A obj = new A(1, pi);
            A.c := 1 ;
            this.a := this.mmain(21) && this.mmain(12);
            return this;
        }

        int fooo(){
            A.a := false;
        }
    }
    """
            expect = """Illegal Member Access: FieldAccess(Id(A),Id(a))"""
            self.assertTrue(TestChecker.test(input, expect, 490))

        def test_91(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            if s + 1 < as then{
                continue;
            }
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    
    """
            expect = """Continue Not In Loop"""
            self.assertTrue(TestChecker.test(input, expect, 491))

        def test_92(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            final int ss = 32;
            final float bb = ss + 1 * 2 - 0.1;
            final int var = ss + 1 * 2 - bb;
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    
    """
            expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(var),IntType,BinaryOp(-,BinaryOp(+,Id(ss),BinaryOp(*,IntLit(1),IntLit(2))),Id(bb)))"""
            self.assertTrue(TestChecker.test(input, expect, 492))

        
        def test_93(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            final int ss = 32;
            final float ba = ss + 1 - 0.2;
            ba := 1e-1;
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    
    """
            expect = """Cannot Assign To Constant: AssignStmt(Id(ba),FloatLit(0.1))"""
            self.assertTrue(TestChecker.test(input, expect, 493))

        
        def test_94(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            final int ss = 32;
            final float ba = ss + 1 - s;
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    
    """
            expect = """Illegal Constant Expression: BinaryOp(-,BinaryOp(+,Id(ss),IntLit(1)),Id(s))"""
            self.assertTrue(TestChecker.test(input, expect, 494))

        
        def test_95(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            final int ss = 32;
            final float ba = ss + 1 - ss;
            for ss := 1 to 10000 do{
                continue;
            }
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    
    """
            expect = """Cannot Assign To Constant: AssignStmt(Id(ss),IntLit(1))"""
            self.assertTrue(TestChecker.test(input, expect, 495))

        def test_96(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            final int ss = 32;
            final float ba = ss + 1 - ss;
            for as := 1 to ba + 10 do{
                continue;
            }
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    
    """
            expect = """Type Mismatch In Statement: For(Id(as),IntLit(1),BinaryOp(+,Id(ba),IntLit(10)),True,Block([],[Continue])])"""
            self.assertTrue(TestChecker.test(input, expect, 496))

        
        def test_97(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            final int ss = 32;
            final float ba = ss + 1 - ss;
            int[3] arr;
            arr := {1,2};
        }
        boolean mmain(int c){
            return this.a;
        }
    }

    
    """
            expect = """Type Mismatch In Statement: AssignStmt(Id(arr),[IntLit(1),IntLit(2)])"""
            self.assertTrue(TestChecker.test(input, expect, 497))


        def test_98(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            final int ss = 32;
            final float ba = ss + 1 - ss;
            float[3] arr;
            arr := {true,false,false};
            arr[1] := true;
        }
        float mmain(int c){
            return A.c;
        }
    }

    
    """
            expect = """Type Mismatch In Statement: AssignStmt(Id(arr),[BooleanLit(True),BooleanLit(False),BooleanLit(False)])"""
            self.assertTrue(TestChecker.test(input, expect, 498))

        def test_99(self):
            input ="""
    class A {
        static float c;
        boolean a;
        A(int as; float s){
            final int ss = 32;
            final float ba = ss + 1 - ss;
            float[3] arr;
            arr := {1,2,3};
            arr[0] := this.mmain(ss,1) + ba;
        }
        float mmain(float c; boolean bb){
            return A.c;
        }
    }

    
    """
            expect = """Type Mismatch In Expression: CallExpr(Self(),Id(mmain),[Id(ss),IntLit(1)])"""
            self.assertTrue(TestChecker.test(input, expect, 499))