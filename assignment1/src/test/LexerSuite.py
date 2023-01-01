import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_2(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_3(self):
        self.assertTrue(TestLexer.test("aAsVN32","aAsVN32,<EOF>",103))
    def test_4(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",104))

    #Start here!
    def test_5(self):
        """test underscore id"""
        self.assertTrue(TestLexer.test("_23_a12_","_23_a12_,<EOF>",105))    
    def test_6(self):
        """test unknown char in id"""
        self.assertTrue(TestLexer.test("akfheK@q","akfheK,Error Token @",106))
    def test_7(self):
        """test unknown char in id"""
        self.assertTrue(TestLexer.test("ak|heKq","ak,Error Token |",107))
    def test_8(self):
        """test many id tokens"""
        self.assertTrue(TestLexer.test("abc def","abc,def,<EOF>",108))
    def test_9(self):
        """test unknown char in id"""
        self.assertTrue(TestLexer.test("abjkabv gega ghei giaw3y gue ve","abjkabv,gega,ghei,giaw3y,gue,ve,<EOF>",109))
    def test_10(self):
        """test int"""
        self.assertTrue(TestLexer.test("1 2 3 4 5 67","1,2,3,4,5,67,<EOF>",110))
    def test_11(self):
        """test int and char id"""
        self.assertTrue(TestLexer.test("12    467  38     a      237v","12,467,38,a,237,v,<EOF>",111))
    def test_12(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.2 0.2 1.23 3.14","1.2,0.2,1.23,3.14,<EOF>",112))
    def test_13(self):
        """test float"""
        self.assertTrue(TestLexer.test("1.12e+2 3.14e-312 12e8 1. 0.33E-3","1.12e+2,3.14e-312,12e8,1.,0.33E-3,<EOF>",113))
    def test_14(self):
        """test float"""
        self.assertTrue(TestLexer.test("1..","1.,.,<EOF>",114))
    def test_15(self):
        """test float"""
        self.assertTrue(TestLexer.test(".12 143e",".,12,143,e,<EOF>",115))
    def test_16(self):
        """test comment line"""
        self.assertTrue(TestLexer.test("#this is a comment","<EOF>",116))
    def test_17(self):
        """test comment line"""
        self.assertTrue(TestLexer.test("#this is a comment # this a cmt","<EOF>",117))
    def test_18(self):
        """test comment block"""
        self.assertTrue(TestLexer.test("/*this is block comt*/","<EOF>",118))
    def test_19(self):
        """ Test comment block """
        self.assertTrue(TestLexer.test(
            """
            /* This is a block cmt */
            /* This is a block cmt */
            ""","<EOF>",119
        ))
    def test_20(self):
        """ Test comment block """
        self.assertTrue(TestLexer.test(
            """
            /* This is a block cmt */
            /* This is a block cmt
            ""","/,*,This,is,a,block,cmt,<EOF>",120
        ))
    def test_21(self):
        """ Test nested block """
        self.assertTrue(TestLexer.test(
            """/* This is /*a block*/ cmt */""","cmt,*,/,<EOF>",121
        ))
    def test_22(self):
        """ Test block comment"""
        self.assertTrue(TestLexer.test(
            """/* This is a block comment so # has no meaning here */""","<EOF>",122
        ))
    def test_23(self):
        """ Test cmt """
        self.assertTrue(TestLexer.test(
            """#This is a line comment so /* has no meaning here""","<EOF>",123
        ))
    def test_24(self):
        """ Test cmt line """
        self.assertTrue(TestLexer.test(
            """a := 5;#this is a line comment""","a,:=,5,;,<EOF>",124
        ))
    def test_25(self):
        """ Test cmt line """
        self.assertTrue(TestLexer.test(
            """#this is a line comment a:=5;""","<EOF>",125
        ))
    def test_26(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("boolean break class continue do else extends float if int new string",
        "boolean,break,class,continue,do,else,extends,float,if,int,new,string,<EOF>",126))
    
    def test_27(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("then for return true false void nil this final static to downto",
        "then,for,return,true,false,void,nil,this,final,static,to,downto,<EOF>",127))
    def test_28(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("boolean foR","boolean,foR,<EOF>",128))
    def test_29(self):
        """test operator"""
        self.assertTrue(TestLexer.test("+ - * / \ %","+,-,*,/,\,%,<EOF>",129))
    def test_30(self):
        """test operator"""
        self.assertTrue(TestLexer.test("!= ==   <=  >=   < >    ||  &&  ! ^ new ","!=,==,<=,>=,<,>,||,&&,!,^,new,<EOF>",130))
    def test_31(self):
        """test operator"""
        self.assertTrue(TestLexer.test(" new +  ++ +++ -- /\ | &","new,+,+,+,+,+,+,-,-,/,\,Error Token |",131))
    def test_32(self):
        """test operator"""
        self.assertTrue(TestLexer.test("-5 + 10 * 102","-,5,+,10,*,102,<EOF>",132))
    def test_33(self):
        """test separator"""
        self.assertTrue(TestLexer.test("( ) { }  ([ []  ; . , :","(,),{,},(,[,[,],;,.,,,:,<EOF>",133))
    def test_34(self):
        """test boolean"""
        self.assertTrue(TestLexer.test("true false F)alse","true,false,F,),alse,<EOF>",134))
    def test_35(self):
        """test string"""
        self.assertTrue(TestLexer.test("""  \"hello antlr4\" """,""""hello antlr4",<EOF>""",135))
    def test_36(self):
        """test string"""
        self.assertTrue(TestLexer.test("""  \"hello antlr4 with tab\\t\" """,""""hello antlr4 with tab\\t",<EOF>""",136))
    def test_37(self):
        """test string"""
        self.assertTrue(TestLexer.test("""  \"hello antlr4 with tab\\t and carriage\\r" """,""""hello antlr4 with tab\\t and carriage\\r",<EOF>""",137))
    def test_38(self):
        """test string"""
        self.assertTrue(TestLexer.test(""" \"He asked me: \\"Where is John?\\"\"""",""""He asked me: \\"Where is John?\\"",<EOF>""",138))
    def test_39(self):
        """test unknown escape sequence"""
        self.assertTrue(TestLexer.test("""   \"Hello \\q \"  ""","""Illegal Escape In String: "Hello \\q""",139)) 
    def test_40(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test("""   \"Hello \\t   ""","""Unclosed String: "Hello \\t   """,140)) 
    def test_41(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test("""   \"bk3sn$#^^2566 /*   ""","""Unclosed String: "bk3sn$#^^2566 /*   """,141)) 
    def test_42(self):
        """test escape sequence"""
        self.assertTrue(TestLexer.test("""\"\\b\\f\\r\\n\\t\\"\\\\\"""",""""\\b\\f\\r\\n\\t\\"\\\\",<EOF>""",142))
    def test_43(self):
        """test arraylit"""
        self.assertTrue(TestLexer.test("{1,2,3,4,5} {6,7,8,9}","{,1,,,2,,,3,,,4,,,5,},{,6,,,7,,,8,,,9,},<EOF>",143)) 
    def test_44(self):
        """test arraylit"""
        self.assertTrue(TestLexer.test("int[3] a={2.3, 4.2, 102e3};","int,[,3,],a,=,{,2.3,,,4.2,,,102e3,},;,<EOF>",144))
    def test_45(self):
        """test array type"""
        self.assertTrue(TestLexer.test("int[5][4] a;","int,[,5,],[,4,],a,;,<EOF>",145))
    def test_46(self):
        """test array type"""
        self.assertTrue(TestLexer.test("bvejint[5]ga[4] a;","bvejint,[,5,],ga,[,4,],a,;,<EOF>",146))
    def test_47(self):
        """test new"""
        self.assertTrue(TestLexer.test("Neural nn = new Neural();","Neural,nn,=,new,Neural,(,),;,<EOF>",147))
    def test_48(self):
        """test new"""
        self.assertTrue(TestLexer.test("int = new()new()lnvaek34newn;","int,=,new,(,),new,(,),lnvaek34newn,;,<EOF>",148))
    def test_49(self):
        """test id name"""
        self.assertTrue(TestLexer.test("int = new() newnewnewintfloat;","int,=,new,(,),newnewnewintfloat,;,<EOF>",149))
    def test_50(self):
        """ Test assign """
        self.assertTrue(TestLexer.test(
            """
            int x;
            x = new X();
            x := x + 1;
            ""","int,x,;,x,=,new,X,(,),;,x,:=,x,+,1,;,<EOF>",150
        ))
    def test_51(self):
        """ Test assign """
        self.assertTrue(TestLexer.test("a[3+x.foo(2)] := a[b[2]] +3;","a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>",151
        ))
    def test_52(self):
        """ Test assign """
        self.assertTrue(TestLexer.test("x.b[2] := x.m()[3];","x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,<EOF>",152
        ))
    def test_53(self):
        """ Test assign  """
        self.assertTrue(TestLexer.test("x.b[2] := x.m()[3];","x,.,b,[,2,],:=,x,.,m,(,),[,3,],;,<EOF>",153
        ))
    def test_54(self):
        """ Test class """
        self.assertTrue(TestLexer.test(
            """
            class goal{}
            ""","class,goal,{,},<EOF>",154
        ))
    def test_55(self):
        """ Test class """
        self.assertTrue(TestLexer.test(
            """
            class Shape {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
            ""","class,Shape,{,static,final,int,numOfShape,=,0,;,final,int,immuAttribute,=,0,;,<EOF>",155
        ))
    def test_56(self):
        """ Test class """
        self.assertTrue(TestLexer.test(
            """
            class Shape {\r
                static final int numOfShape = 0;    \t#Cmtt
                final int immuAttribute = 0;}
            ""","class,Shape,{,static,final,int,numOfShape,=,0,;,final,int,immuAttribute,=,0,;,},<EOF>",156
        ))
    def test_57(self):
        """ Test class """
        self.assertTrue(TestLexer.test(
            """
            class Shape {
                static final int numOfShape = 0;    #Cmtt
                final int immuAttribute = 0;
                float length,width;
                static int getNumOfShape() {
                    return numOfShape;
                }

            }
            ""","class,Shape,{,static,final,int,numOfShape,=,0,;,final,int,immuAttribute,=,0,;,float,length,,,width,;,static,int,getNumOfShape,(,),{,return,numOfShape,;,},},<EOF>",157
        ))
    
    def test_58(self):
        """ Test class extends """
        self.assertTrue(TestLexer.test(
            """
            class Shape extends ABC{
                static final int numOfShape = 0;    #Cmtt
                final int immuAttribute = 0;}
            ""","class,Shape,extends,ABC,{,static,final,int,numOfShape,=,0,;,final,int,immuAttribute,=,0,;,},<EOF>",158
        ))
    def test_59(self):
        """ Test class extends """
        self.assertTrue(TestLexer.test(
            """
            class Rectangle extends Shape {
                float getArea(){
                    return this.length*this.width;
                }
            }
            ""","class,Rectangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>",159
        ))
    def test_60(self):
        """ Test io """
        self.assertTrue(TestLexer.test(
            "io.writeStrLn(\"hello antlr4\");","io,.,writeStrLn,(,\"hello antlr4\",),;,<EOF>",160
        ))
    def test_61(self):
        """ Test expr """
        self.assertTrue(TestLexer.test(
            "int a = (1+2*3/4%5)*(1.2%2.3)","int,a,=,(,1,+,2,*,3,/,4,%,5,),*,(,1.2,%,2.3,),<EOF>",161
        ))
    def test_62(self):
        """ Test class unclosed """
        self.assertTrue(TestLexer.test(
            "class a{","class,a,{,<EOF>",162
        ))
    def test_63(self):
        """ Test object """
        self.assertTrue(TestLexer.test(
            "Shape a = new Shape(1,2,3,4,5,7,@)","Shape,a,=,new,Shape,(,1,,,2,,,3,,,4,,,5,,,7,,,Error Token @",163
        ))
    def test_64(self):
        """ Test concat """
        self.assertTrue(TestLexer.test("\"hello\"  ^   \"antlr4\" ","\"hello\",^,\"antlr4\",<EOF>",164))
    def test_65(self):
        """ Test illegal char \r in string """
        self.assertTrue(TestLexer.test(
            "\"hello\r\"^\"antlr4\"","""Unclosed String: "hello""",165
        ))
    def test_66(self):
        """ Test illegal char \n in string """
        self.assertTrue(TestLexer.test(
            "\"hello\"^\"antlr4\n\"","""\"hello\",^,Unclosed String: \"antlr4""",166
        ))
        
    def test_67(self):
        """ Test legal char \t in string """
        self.assertTrue(TestLexer.test(
            "\"hello\t\"^\"antlr4\t\"","\"hello	\",^,\"antlr4	\",<EOF>",167
        ))
    def test_68(self):
        """ Test operator tokens """
        self.assertTrue(TestLexer.test(
            "<=> <!=>=:==>","<=,>,<,!=,>=,:=,=,>,<EOF>",168
        ))
    def test_69(self):
        """ Test if """
        self.assertTrue(TestLexer.test(
            "if flag then a:=a+1;","if,flag,then,a,:=,a,+,1,;,<EOF>",169
        ))
    def test_70(self):
        """ Test if else"""
        self.assertTrue(TestLexer.test(
            "if flag then a:=a+1 else a:= a+2;","if,flag,then,a,:=,a,+,1,else,a,:=,a,+,2,;,<EOF>",170
        ))
    def test_71(self):
        """ Test if else"""
        self.assertTrue(TestLexer.test(
            "if flag then a:=a+1 else {a:= a+2;a:=a*2;};","if,flag,then,a,:=,a,+,1,else,{,a,:=,a,+,2,;,a,:=,a,*,2,;,},;,<EOF>",171
        ))
    def test_72(self):
        """ Test if else"""
        self.assertTrue(TestLexer.test(
            "if flag then a:=a+1 else if {a:= a+2;a:=a*2;} else;","if,flag,then,a,:=,a,+,1,else,if,{,a,:=,a,+,2,;,a,:=,a,*,2,;,},else,;,<EOF>",172
        ))
    def test_73(self):
        """ Test if else"""
        self.assertTrue(TestLexer.test(
            "if (a&&b || Treu) then a:=a+1 else {a:= a+2;a:=a*2;};","if,(,a,&&,b,||,Treu,),then,a,:=,a,+,1,else,{,a,:=,a,+,2,;,a,:=,a,*,2,;,},;,<EOF>",173
        ))
    def test_74(self):
        """ Test for"""
        self.assertTrue(TestLexer.test(
            "for i := 1 to 100 do pushup;","for,i,:=,1,to,100,do,pushup,;,<EOF>",174
        ))
    def test_75(self):
        """ Test for"""
        self.assertTrue(TestLexer.test(
            "for i := 1 to 100 do {bnekb a[21] := k[1] / 12 || True && False}","for,i,:=,1,to,100,do,{,bnekb,a,[,21,],:=,k,[,1,],/,12,||,True,&&,False,},<EOF>",175
        ))
    def test_76(self):
        """ Test for"""
        self.assertTrue(TestLexer.test(
            "for i := 1 downto 100 do pushup;","for,i,:=,1,downto,100,do,pushup,;,<EOF>",176
        ))
    def test_77(self):
        """ Test for"""
        self.assertTrue(TestLexer.test(
            """for i := 1 to 100 do {
                io.writeIntLn(i);
                Intarray[i] := i + 1;
                }""","for,i,:=,1,to,100,do,{,io,.,writeIntLn,(,i,),;,Intarray,[,i,],:=,i,+,1,;,},<EOF>",177
        ))
    def test_78(self):
        """ Test for"""
        self.assertTrue(TestLexer.test(
            """for i := 100 - nevn 100 do {
                io.writeIntLn(i);
                Intarray[i] := i + 1;
                }""","for,i,:=,100,-,nevn,100,do,{,io,.,writeIntLn,(,i,),;,Intarray,[,i,],:=,i,+,1,;,},<EOF>",178
        ))
    def test_79(self):
        """ Test for"""
        self.assertTrue(TestLexer.test(
            """break for i := 100 - nevn 100 do {break;break;break;
                io.writeIntLn(i);
                Intarray[i] := i + 1;
                }""","break,for,i,:=,100,-,nevn,100,do,{,break,;,break,;,break,;,io,.,writeIntLn,(,i,),;,Intarray,[,i,],:=,i,+,1,;,},<EOF>",179
        ))
    def test_80(self):
        """ Test for"""
        self.assertTrue(TestLexer.test(
            """break for i := 100 - nevn 100 do {break;Break;break;
                io.writeIntLn(i);
                continue;
                Intarray[i] := i + 1; Shape a = new Shape(new Shape(12), a[12][12]);
                Continue;
                }""","break,for,i,:=,100,-,nevn,100,do,{,break,;,Break,;,break,;,io,.,writeIntLn,(,i,),;,continue,;,Intarray,[,i,],:=,i,+,1,;,Shape,a,=,new,Shape,(,new,Shape,(,12,),,,a,[,12,],[,12,],),;,Continue,;,},<EOF>",180
        ))
    def test_81(self):
        """ Test class extends and invocation """
        self.assertTrue(TestLexer.test(
            """
            class Rectangle extends Shape {
                float getArea(){
                    return this.length*this.width;
                }
                Rectangle a = new Rectangle()
                a.getArea();
            }
            ""","class,Rectangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},Rectangle,a,=,new,Rectangle,(,),a,.,getArea,(,),;,},<EOF>",181))
    def test_82(self):
        """ Test class extends and invocation """
        self.assertTrue(TestLexer.test(
            """
            class Example2 {
                void main(){
                s:Shape;
                s := new Rectangle(3,4);
                io.writeFloatLn(s.getArea());
                s := new Triangle(3,4);
                io.writeFloatLn(s.getArea());
                }
            }
        ""","class,Example2,{,void,main,(,),{,s,:,Shape,;,s,:=,new,Rectangle,(,3,,,4,),;,io,.,writeFloatLn,(,s,.,getArea,(,),),;,s,:=,new,Triangle,(,3,,,4,),;,io,.,writeFloatLn,(,s,.,getArea,(,),),;,},},<EOF>",182))
    def test_83(self):
        """ Test for"""
        self.assertTrue(TestLexer.test(
            """{
            #start of declaration part
            float r,s;
            int[5] a,b;
        #   list of statements
            r:=2.0;
        s:=r*r*this.myPI;
            a[0]:= s;
            }""","{,float,r,,,s,;,int,[,5,],a,,,b,;,r,:=,2.0,;,s,:=,r,*,r,*,this,.,myPI,;,a,[,0,],:=,s,;,},<EOF>",183
        ))
    def test_84(self):
        """test operator"""
        self.assertTrue(TestLexer.test("\"/\//\\//\"","Illegal Escape In String: \"/\/",184))
    def test_85(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"Hello1\" ba ek ske  \"","\"Hello1\",ba,ek,ske,Unclosed String: \"",185))
    def test_86(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"Hello1\" ba ek ske  \" abc","\"Hello1\",ba,ek,ske,Unclosed String: \" abc",186))
    def test_87(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"Hello1\" ba ek ske  \" abc","\"Hello1\",ba,ek,ske,Unclosed String: \" abc",187))
    def test_88(self):
        """test operator"""
        self.assertTrue(TestLexer.test("!^a v^gwg^^&*)(h^ave!!!+=-#^e^!","!,^,a,v,^,gwg,^,^,Error Token &",188))
    def test_89(self):
        """test cmt"""
        self.assertTrue(TestLexer.test("/*/*/*/*/*/*######vjqbvbq####*/","*,*,<EOF>",189))
    def test_90(self):
        """test array"""
        self.assertTrue(TestLexer.test("{     \"124\" ,     \"21\"     ,      \"423\"   }","{,\"124\",,,\"21\",,,\"423\",},<EOF>",190))
    def test_91(self):
        """test this"""
        self.assertTrue(TestLexer.test("this.area := 100","this,.,area,:=,100,<EOF>",191))
    def test_92(self):
        """test this"""
        self.assertTrue(TestLexer.test("this.area := this.area := this.area := 100","this,.,area,:=,this,.,area,:=,this,.,area,:=,100,<EOF>",192))
    def test_93(self):
        """test"""
        self.assertTrue(TestLexer.test("avb avbej ave #@@@","avb,avbej,ave,<EOF>",193))
    def test_94(self):
        """test"""
        self.assertTrue(TestLexer.test("_______a____:= 100","_______a____,:=,100,<EOF>",194))
    def test_95(self):
        """test"""
        self.assertTrue(TestLexer.test("t_t+u=new shape () ?/*?*/ ","t_t,+,u,=,new,shape,(,),Error Token ?",195))
    def test_96(self):
        """test"""
        self.assertTrue(TestLexer.test("\"######################*?*?\"","\"######################*?*?\",<EOF>",196))
    def test_97(self):
        """test"""
        self.assertTrue(TestLexer.test(":=1.3e1",":=,1.3e1,<EOF>",197))
    def test_98(self):
        """test"""
        self.assertTrue(TestLexer.test(":=1.3e ",":=,1.3,e,<EOF>",198))
    def test_99(self):
        """test"""
        self.assertTrue(TestLexer.test("","<EOF>",199))
    def test_100(self):
        """test"""
        self.assertTrue(TestLexer.test("the end <The End> \"The end\" t1h2e34e5n6d.||&&%#IKJJKIGGKJBubvkserukb\t ","the,end,<,The,End,>,\"The end\",t1h2e34e5n6d,.,||,&&,%,<EOF>",200))
    
    
    