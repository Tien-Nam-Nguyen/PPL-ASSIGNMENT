import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,203))

    #Start here
    def test_4(self):
        """"""
        input = """class A{"""
        expect = "Error on line 1 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_5(self):
        """"""
        input = """class A}"""
        expect = "Error on line 1 col 7: }"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_6(self):
        """"""
        input = """
        class A{
            int a;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_7(self):
        """"""
        input = """
        class A{
            int a,b;
            float c = 1.2e6;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_8(self):
        """"""
        input = """
        class B{}
        class A extends B{
            int a,b;
            float c = 1.2e6;
            A(){}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_9(self):
        """"""
        input = """
        class B{}
        class A extends {
            int a,b;
            float c = 1.2e6
        }
        """
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_10(self):
        """"""
        input = """
        class B{}
        class A extends B extends C{
            int a,b;
            float c = 1.2e6
        }
        """
        expect = "Error on line 3 col 26: extends"
        self.assertTrue(TestParser.test(input,expect,210))
    
    def test_11(self):
        """"""
        input = """
        class B{}
        class A extends B /*extends C*/{
            int a,b;
            float c = 1.2e6;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_12(self):
        """"""
        input = """
        class B{}
        class A extends B{
            int a=1,b=3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_13(self):
        """"""
        input = """
        class A extends B{
            int a=1,b=3;c=4;
        }
        """
        expect = "Error on line 3 col 25: ="
        self.assertTrue(TestParser.test(input,expect,213))

    def test_14(self):
        input = """
class A{
    A(int A){
        io.writeInt();
        int x;
    }
}
"""
        expect = "Error on line 5 col 8: int"
        self.assertTrue(TestParser.test(input, expect, 214))
    
    def test_15(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                int b = 5;
                float c = 12.2;
            }
            int a = 10;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_16(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                int b = 5;
                float c = 12.2;
                if (b==5) then{
                    io.writeInt();
                }
                else{}
            }
            int a = 10;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_17(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                int b = 5;
                float c = 12.2;
                if (b==5) then{
                    io.writeInt();
                }
                else #No else
            }
            int a = 10;
        }
        """
        expect = "Error on line 10 col 12: }"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_18(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                int b = 5;
                float c = 12.2;
                c := 10;
                return c;
            }
            int a = 10;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_19(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                int b = 5;
                float c = 12.2;
                c := 10;
                return this.c * this.b;
            }
            int a = 10;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_20(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                int b = 5;
                float c = 12.2;
                c := 10;
                return this[2] * this.b;
            }
            int a = 10;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_21(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                int b = 5;
                float c = 12.2;
                c := 10;
            }
            int a = 10;
            class B{}
        }
        """
        expect = "Error on line 9 col 12: class"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_22(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                class B{}
                int b = 5;
                float c = 12.2;
                c := 10;
            }
            int a = 10;
        }
        """
        expect = "Error on line 4 col 16: class"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_23(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                string a = "a"^"b";
                int b = 5;
                float c = 12.2
                c := 10
            }
        }
        """
        expect = "Error on line 7 col 16: c"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_24(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                string a = "a"^"b";
                a := 12;
                int b = 5;
                b:=6;
                float c = 12.2;
            }
        }
        """
        expect = "Error on line 6 col 16: int"
        self.assertTrue(TestParser.test(input,expect,224))      
    def test_25(self):
        """"""
        input = """
        class A extends B{
            A(int a){
                string a = "a"^"b";
                a := 12;
                b:=6;
            }
            void main(){
                this.A();   /*fjjhjvbjve*/
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_26(self):
        """"""
        input = """
        class A extends B{
            static final int a;
            final static int b;
            static int c;
            final string d;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_27(self):
        """"""
        input = """
        class A extends B{
            static final int a;
            final static static int b;
            static int c
            final string d;
        }
        """
        expect = "Error on line 4 col 25: static"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_28(self):
        """"""
        input = """
        class A extends B{
            static final int a;
            final static int b;
            static c;
            final string d;
        }
        """
        expect = "Error on line 5 col 20: ;"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_29(self):
        """"""
        input = """
        class A extends B{
            static final int a;
            final static int b;
            static int c := 12; #int d:=12;
        }
        """
        expect = "Error on line 5 col 25: :="
        self.assertTrue(TestParser.test(input,expect,229)) 
    def test_30(self):
        """"""
        input = """
        class A extends B{
            static final int true;
        }
        """
        expect = "Error on line 3 col 29: true"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_31(self):
        """"""
        input = """
        class A extends B{
            void a=12;
        }
        """
        expect = "Error on line 3 col 18: ="
        self.assertTrue(TestParser.test(input,expect,231))
    def test_32(self):
        """"""
        input = """
        class A extends B{
            void void = 12;
        }
        """
        expect = "Error on line 3 col 17: void"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_33(self):
        """"""
        input = """
        class A extends B{
            static int final a = 12;
        }
        """
        expect = "Error on line 3 col 23: final"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_34(self):
        """"""
        input = """
        class A extends B{
            static final A a = new B(new C(), 12, 8), b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    
    def test_35(self):
        """"""
        input = """
        class Example1 {
            int factorial(int n){
                if n == 0 then return 1; else return n * this.factorial(n - 1);
            }
            void main(){
                int x;
                x := io.readInt();
                io.writeIntLn(this.factorial(x));
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_36(self):
        """"""
        input = """
        class Example1 {
            static int a;
            void main(){
                int x;
                x := x + x[5] && True * False % 123e9;
                x := io.readInt();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_37(self):
        """"""
        input = """
        class Example1 {
            static int a;
            void main(){
                int      x,y=12,Int,FloAT,t=100;
            
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_38(self):
        """"""
        input = """
        class Example1 extends string{
            static int a;
            void main(){
                int      x,y=12,Int,FloAT,t=100;
            
            }
        }
        """
        expect = "Error on line 2 col 31: string"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_39(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            void main(){
                int[5] a = 12;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_40(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            void main(){
                int[5] a = {12,3,45
            }
        }
        """
        expect = "Error on line 7 col 8: }"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_41(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            void main(){
                int[5] a = {12,3,45
            };
        }
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_42(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;}
        }
        """
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_43(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            void main(){}
            Example1(){}
            int count{}
        }
        """
        expect = "Error on line 6 col 21: {"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_44(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            void main(){{{{{{{a:=12;}}}}}}}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_45(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            void main(){
                a := b:= c := 10;
            }
        }
        """
        expect = "Error on line 6 col 22: :="
        self.assertTrue(TestParser.test(input,expect,245))
    def test_46(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            void main(){{{{{{{{a:=1;}}}}}}}
        }
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_47(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            void main(){{{{{{{{;}}}}}}}}
        }
        """
        expect = "Error on line 5 col 31: ;"
        self.assertTrue(TestParser.test(input,expect,247))
    
    def test_48(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            void main(){int[5][2] a;}
        }
        """
        expect = "Error on line 5 col 30: ["
        self.assertTrue(TestParser.test(input,expect,248))

    def test_49(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            void main(){int[5]                         a={1,2,3,4,5,1, 1, 1e2,true,"adv"};}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_50(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            void main(){int[5]                         a={1,2,3,4,5,abc,new ID(), &&, a.b(12,11),a[1]};}
        }
        """
        expect = "Error on line 5 col 68: abc"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_51(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            void main(){int[5.] a={1,2,3,4,5,abc,new ID(),a.b(12,11),a[1]};}
        }
        """
        expect = "Error on line 5 col 28: 5."
        self.assertTrue(TestParser.test(input,expect,251))
    def test_52(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            static void main(){}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_53(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            final void main(){int[5] a={1,2,3,4,5,abc,new ID(),a.b(12,11),a[1]};}
        }
        """
        expect = "Error on line 5 col 18: void"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_54(self):
        """"""
        input = """
        class Example1 extends math{
            static int a;
            final float b;
            static static void main(){int[5] a={1,2,3,4,5,abc,new ID(),a.b(12,11),a[1]};}
        }
        """
        expect = "Error on line 5 col 19: static"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_55(self):
        """"""
        input = """
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
                s:Shape;
                s := new Rectangle(3,4);
                io.writeFloatLn(s.getArea());
                s := new Triangle(3,4);
                io.writeFloatLn(s.getArea());
            }
        }
        """
        expect = "Error on line 14 col 17: :"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_56(self):
        """"""
        input = """
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_57(self):
        """"""
        input = """
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
                Shape s = new Shape().shape;
                s := new Rectangle(3,4);
                s := new Triangle(3,4);
                if s == 12 then io.writeInt();
                io.writeFloatLn(s.getArea());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_58(self):
        """"""
        input = """
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
                Shape s = new Shape().shape;
                s := new Rectangle(3,4);
                for i:=1 to 100 do{
                    s:=1;
                    int a=2;
                }
            }
        }
        """
        expect = "Error on line 18 col 20: int"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_59(self):
        """"""
        input = """
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
                Shape s = new Shape().shape;
                s := new Rectangle(3,4);
                for i:=1 to 100 do{
                    break;break;continue;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_60(self):
        """"""
        input = """
        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width[0];
            }
        }
        class Example2 {
            void main(){
                Shape s = new Shape().shape;
                s := new Rectangle();
                if s then for i:=1 to 100 do{} else{if true then {}}
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_61(self):
        """"""
        input = """
        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width;
            }
        }
        class Example2 {
            void main(){
                Shape s = new Shape().shape;
                s := new Rectangle(3,4);
                return s; #s:=1;;;;;;;;;;;;;;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_62(self):
        """"""
        input = """
        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width;
            }
        }
        class Example2 {
            void main(){
                Shape s = new Shape().shape.a(b.ba(bb.bbas(c.c)));
                return s;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_63(self):
        """"""
        input = """
        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width;
            }
        }
        class Example2 {
            void main(){
                Shape s = new Shape();
                a[3+x.foo(2)] := a[b[2]] +3;
                return s;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_64(self):
        """"""
        input = """
        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width[1][2];
            }
        }
        """
        expect = "Error on line 4 col 48: ["
        self.assertTrue(TestParser.test(input,expect,264))
    def test_65(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s){
                return this.length*this.width[a[b[c[d[e[1]]]]]];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_66(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s){
                return this.length*this.width[a[b[c[d[e[1]]]]];
            }
        }
        """
        expect = "Error on line 4 col 62: ;"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_67(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s){
                return this.length*this.width[a[b[c[d[e[1]]]]];
            }
        }
        """
        expect = "Error on line 4 col 62: ;"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_68(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s){
                return this.float;
            }
        }
        """
        expect = "Error on line 4 col 28: float"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_69(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s){
                return a.this(3);
            }
        }
        """
        expect = "Error on line 4 col 25: this"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_70(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s){
                return a.true();
            }
        }
        """
        expect = "Error on line 4 col 25: true"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_71(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s){
                return a[12].b;                     #Phan tu cua mang a la kieu class co attr b
            }
        }
        """
        expect = "Error on line 4 col 28: ."
        self.assertTrue(TestParser.test(input,expect,271))
    def test_72(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s){
                x.b[2] := x.m()[3];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_73(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t; float a,b ; string s;){
            }
        }
        """
        expect = "Error on line 3 col 56: )"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_74(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t, float a,b , string s){
            }
        }
        """
        expect = "Error on line 3 col 35: float"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_75(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t){
                1 := 2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_76(self):
        """"""
        input = """
        class Rectangle{
            float getArea(int x,t){
                this.a[12] := 12;
                this.a.b.c.d.e();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    
    def test_77(self):
         input = """
         class foo {
            Ab[5] n = this.Geometry(x.foo(5)[4]*(!m) + (s >= m || m+-n));
            H[5] function(A a,b,c; H n){
                 int k = 9;
                 m := n;
                 int n;
             }
         }
         """
         expect = """Error on line 7 col 17: int"""
         self.assertTrue(TestParser.test(input, expect, 277))   
    def test_78(self):
         input = """
         class foo {
            H[5] function(A a,b,c; H n){
                 int k = 9;
                 m := n := k := 4e;
             }
         }
         """
         expect = """Error on line 5 col 24: :="""
         self.assertTrue(TestParser.test(input, expect, 278)) 
    def test_79(self):
         input = """
         class foo {
            #Just a comment with fake }
             
         }
         """
         expect = """successful"""
         self.assertTrue(TestParser.test(input, expect, 279))
    def test_80(self):
         input = """
         class A{}
         class foo {
            #Just a comment with fake }
            int A = foo; 
         }
         """

         expect = """successful"""
         self.assertTrue(TestParser.test(input, expect, 280))
    def test_81(self):
         input = """
         class A{}
         class foo {
            #Just a comment with fake }
            A == foo;
         }
         """

         expect = """Error on line 5 col 14: =="""
         self.assertTrue(TestParser.test(input, expect, 281))
    def test_82(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
                this.a[12] := 12;
                this.a.b.c.d.e();
                12 + 12 + True;
            }
        }
        """
        expect = "Error on line 6 col 19: +"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_83(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
                this.a[12] := a.this;
            }
        }
        """
        expect = "Error on line 4 col 32: this"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_84(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
                this.a[12] := 12.this;
            }
        }
        """
        expect = "Error on line 4 col 33: this"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_85(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
                this.a[12] := new[12];
            }
        }
        """
        expect = "Error on line 4 col 33: ["
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_86(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
                this.ab.c := (1||2 := 3);
            }
        }
        """
        expect = "Error on line 4 col 35: :="
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_87(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
                this.ab.c := (1||23);
            }
        }
        class Triangle{
            if class > 1 then 1 := 1;
        }
        """
        expect = "Error on line 8 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_88(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
                this.ab.c := (1||23);
            }
        }
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                return true;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
            }
        }
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a := a == 1 >= 12 != 3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
            }
        }
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a := a == 1 == 3;
            }
        }
        """
        expect = "Error on line 9 col 28: =="
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
            }
        }
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a := a == 1 != 3;
            }
        }
        """
        expect = "Error on line 9 col 28: !="
        self.assertTrue(TestParser.test(input, expect, 291))
    
    def test_92(self):
        input = """
        class Rectangle{
            float getArea(int x,t){
            }
        }
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a := a == 1 >= 3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    
    def test_93(self):
        input = """
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a := a == 1 != 3;
            }
        }
        """
        expect = "Error on line 5 col 28: !="
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_94(self):
        input = """
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a := (a == 1) != 3;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    
    def test_95(self):
        input = """
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a := a == (1 (==) (3));
            }
        }
        """
        expect = "Error on line 5 col 29: ("
        self.assertTrue(TestParser.test(input, expect, 295))
    
    def test_96(self):
        input = """
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a := (a.b).c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    
    def test_97(self):
        input = """
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a:=a;
                return a;a.void(12);
            }
        }
        """
        expect = "Error on line 6 col 27: void"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98(self):
        input = """
        class Triangle{
            boolean truEnewFaLse = 1e6;
            int geth(string Stringnew){
                a:=a;
                return a;
            }
        }
        class shape extends 12.01{
            
        }
        """
        expect = "Error on line 9 col 28: 12.01"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input = """
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
                s := new Rectangle(3,4);
                io.writeFloatLn(s.getArea());
                s := new Triangle(3,4);
                io.writeFloatLn(s.getArea());
            }
            int get(){
                return this.s[12+12];
            }
            int set(){
                this.sa := a[0.5];
                for i:=10000 downto 1 do{
                    for j:=1 to 10000 do{
                        for k:=-1 to true || false do{
                            if true then {} else {}
                        }
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    

    def test_100(self):
        input = """
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
                s := new Rectangle(3,4);
                io.writeFloatLn(s.getArea());
                s := new Triangle(3,4);
                io.writeFloatLn(s.getArea());
            }
            int get(){
                return this.s[12+12];
            }
            int set(){
                this.sa := a[new Shape().set().get().attribute == 12];
                for i:=10000 downto 1 do{
                    for j:=1 to 10000 do{
                        for k:=-1 to true || false do{
                            if true then {} else {}
                        }
                    }
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))