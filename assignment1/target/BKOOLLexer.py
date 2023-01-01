# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\3\6\3\u008f\n\3\r\3\16\3\u0090")
        buf.write("\3\4\3\4\3\4\5\4\u0096\n\4\3\4\5\4\u0099\n\4\3\5\6\5\u009c")
        buf.write("\n\5\r\5\16\5\u009d\3\6\3\6\7\6\u00a2\n\6\f\6\16\6\u00a5")
        buf.write("\13\6\3\7\3\7\5\7\u00a9\n\7\3\7\6\7\u00ac\n\7\r\7\16\7")
        buf.write("\u00ad\3\b\3\b\5\b\u00b2\n\b\3\t\3\t\7\t\u00b6\n\t\f\t")
        buf.write("\16\t\u00b9\13\t\3\t\3\t\3\n\3\n\3\n\5\n\u00c0\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d7")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3>\3?\3?\7?\u019d\n?\f?\16?\u01a0")
        buf.write("\13?\3@\3@\3@\3@\7@\u01a6\n@\f@\16@\u01a9\13@\3@\3@\3")
        buf.write("@\3@\3@\3A\3A\7A\u01b2\nA\fA\16A\u01b5\13A\3A\3A\3B\6")
        buf.write("B\u01ba\nB\rB\16B\u01bb\3B\3B\3C\3C\7C\u01c2\nC\fC\16")
        buf.write("C\u01c5\13C\3C\5C\u01c8\nC\3C\5C\u01cb\nC\3C\3C\3D\3D")
        buf.write("\7D\u01d1\nD\fD\16D\u01d4\13D\3D\3D\3D\3D\3E\3E\3E\3\u01a7")
        buf.write("\2F\3\3\5\4\7\5\t\2\13\2\r\2\17\6\21\7\23\2\25\b\27\t")
        buf.write("\31\n\33\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25")
        buf.write("\61\26\63\27\65\30\67\319\32;\33=\34?\35A\36C\37E G!I")
        buf.write("\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65")
        buf.write("q\66s\67u8w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087A\u0089")
        buf.write("B\3\2\f\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\16\17$$^^\t\2")
        buf.write("$$^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\16\17")
        buf.write("\5\2\13\f\16\17\"\"\3\2$$\2\u01eb\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b")
        buf.write("\3\2\2\2\5\u008e\3\2\2\2\7\u0092\3\2\2\2\t\u009b\3\2\2")
        buf.write("\2\13\u009f\3\2\2\2\r\u00a6\3\2\2\2\17\u00b1\3\2\2\2\21")
        buf.write("\u00b3\3\2\2\2\23\u00bf\3\2\2\2\25\u00d6\3\2\2\2\27\u00d8")
        buf.write("\3\2\2\2\31\u00e0\3\2\2\2\33\u00e6\3\2\2\2\35\u00ec\3")
        buf.write("\2\2\2\37\u00f5\3\2\2\2!\u00f8\3\2\2\2#\u00fd\3\2\2\2")
        buf.write("%\u0105\3\2\2\2\'\u010b\3\2\2\2)\u010e\3\2\2\2+\u0112")
        buf.write("\3\2\2\2-\u0116\3\2\2\2/\u011d\3\2\2\2\61\u0122\3\2\2")
        buf.write("\2\63\u0126\3\2\2\2\65\u012d\3\2\2\2\67\u0132\3\2\2\2")
        buf.write("9\u0137\3\2\2\2;\u013d\3\2\2\2=\u0141\3\2\2\2?\u0146\3")
        buf.write("\2\2\2A\u014c\3\2\2\2C\u0153\3\2\2\2E\u0156\3\2\2\2G\u015d")
        buf.write("\3\2\2\2I\u015f\3\2\2\2K\u0161\3\2\2\2M\u0163\3\2\2\2")
        buf.write("O\u0165\3\2\2\2Q\u0167\3\2\2\2S\u0169\3\2\2\2U\u016c\3")
        buf.write("\2\2\2W\u016f\3\2\2\2Y\u0171\3\2\2\2[\u0173\3\2\2\2]\u0176")
        buf.write("\3\2\2\2_\u0179\3\2\2\2a\u017c\3\2\2\2c\u017f\3\2\2\2")
        buf.write("e\u0181\3\2\2\2g\u0183\3\2\2\2i\u0185\3\2\2\2k\u0187\3")
        buf.write("\2\2\2m\u0189\3\2\2\2o\u018b\3\2\2\2q\u018d\3\2\2\2s\u018f")
        buf.write("\3\2\2\2u\u0191\3\2\2\2w\u0193\3\2\2\2y\u0195\3\2\2\2")
        buf.write("{\u0197\3\2\2\2}\u019a\3\2\2\2\177\u01a1\3\2\2\2\u0081")
        buf.write("\u01af\3\2\2\2\u0083\u01b9\3\2\2\2\u0085\u01bf\3\2\2\2")
        buf.write("\u0087\u01ce\3\2\2\2\u0089\u01d9\3\2\2\2\u008b\u008c\7")
        buf.write("?\2\2\u008c\4\3\2\2\2\u008d\u008f\t\2\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\6\3\2\2\2\u0092\u0098\5\t\5\2\u0093")
        buf.write("\u0095\5\13\6\2\u0094\u0096\5\r\7\2\u0095\u0094\3\2\2")
        buf.write("\2\u0095\u0096\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0099")
        buf.write("\5\r\7\2\u0098\u0093\3\2\2\2\u0098\u0097\3\2\2\2\u0099")
        buf.write("\b\3\2\2\2\u009a\u009c\t\2\2\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\n\3\2\2\2\u009f\u00a3\7\60\2\2\u00a0\u00a2\t\2")
        buf.write("\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\f\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a6\u00a8\t\3\2\2\u00a7\u00a9\t\4\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2")
        buf.write("\u00aa\u00ac\t\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3")
        buf.write("\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\16")
        buf.write("\3\2\2\2\u00af\u00b2\5\67\34\2\u00b0\u00b2\59\35\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\20\3\2\2\2\u00b3")
        buf.write("\u00b7\7$\2\2\u00b4\u00b6\5\23\n\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb")
        buf.write("\7$\2\2\u00bb\22\3\2\2\2\u00bc\u00c0\n\5\2\2\u00bd\u00be")
        buf.write("\7^\2\2\u00be\u00c0\t\6\2\2\u00bf\u00bc\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00c0\24\3\2\2\2\u00c1\u00c2\7Y\2\2\u00c2")
        buf.write("\u00c3\7t\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7v\2\2\u00c5")
        buf.write("\u00c6\7g\2\2\u00c6\u00c7\7N\2\2\u00c7\u00d7\7p\2\2\u00c8")
        buf.write("\u00c9\7y\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb")
        buf.write("\u00cc\7v\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7n\2\2\u00ce")
        buf.write("\u00d7\7p\2\2\u00cf\u00d0\7Y\2\2\u00d0\u00d1\7T\2\2\u00d1")
        buf.write("\u00d2\7K\2\2\u00d2\u00d3\7V\2\2\u00d3\u00d4\7G\2\2\u00d4")
        buf.write("\u00d5\7N\2\2\u00d5\u00d7\7P\2\2\u00d6\u00c1\3\2\2\2\u00d6")
        buf.write("\u00c8\3\2\2\2\u00d6\u00cf\3\2\2\2\u00d7\26\3\2\2\2\u00d8")
        buf.write("\u00d9\7d\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7q\2\2\u00db")
        buf.write("\u00dc\7n\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7c\2\2\u00de")
        buf.write("\u00df\7p\2\2\u00df\30\3\2\2\2\u00e0\u00e1\7d\2\2\u00e1")
        buf.write("\u00e2\7t\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7c\2\2\u00e4")
        buf.write("\u00e5\7m\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\7e\2\2\u00e7")
        buf.write("\u00e8\7n\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7u\2\2\u00ea")
        buf.write("\u00eb\7u\2\2\u00eb\34\3\2\2\2\u00ec\u00ed\7e\2\2\u00ed")
        buf.write("\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7v\2\2\u00f0")
        buf.write("\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3\7w\2\2\u00f3")
        buf.write("\u00f4\7g\2\2\u00f4\36\3\2\2\2\u00f5\u00f6\7f\2\2\u00f6")
        buf.write("\u00f7\7q\2\2\u00f7 \3\2\2\2\u00f8\u00f9\7g\2\2\u00f9")
        buf.write("\u00fa\7n\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc\7g\2\2\u00fc")
        buf.write("\"\3\2\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7z\2\2\u00ff")
        buf.write("\u0100\7v\2\2\u0100\u0101\7g\2\2\u0101\u0102\7p\2\2\u0102")
        buf.write("\u0103\7f\2\2\u0103\u0104\7u\2\2\u0104$\3\2\2\2\u0105")
        buf.write("\u0106\7h\2\2\u0106\u0107\7n\2\2\u0107\u0108\7q\2\2\u0108")
        buf.write("\u0109\7c\2\2\u0109\u010a\7v\2\2\u010a&\3\2\2\2\u010b")
        buf.write("\u010c\7k\2\2\u010c\u010d\7h\2\2\u010d(\3\2\2\2\u010e")
        buf.write("\u010f\7k\2\2\u010f\u0110\7p\2\2\u0110\u0111\7v\2\2\u0111")
        buf.write("*\3\2\2\2\u0112\u0113\7p\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("\u0115\7y\2\2\u0115,\3\2\2\2\u0116\u0117\7u\2\2\u0117")
        buf.write("\u0118\7v\2\2\u0118\u0119\7t\2\2\u0119\u011a\7k\2\2\u011a")
        buf.write("\u011b\7p\2\2\u011b\u011c\7i\2\2\u011c.\3\2\2\2\u011d")
        buf.write("\u011e\7v\2\2\u011e\u011f\7j\2\2\u011f\u0120\7g\2\2\u0120")
        buf.write("\u0121\7p\2\2\u0121\60\3\2\2\2\u0122\u0123\7h\2\2\u0123")
        buf.write("\u0124\7q\2\2\u0124\u0125\7t\2\2\u0125\62\3\2\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127\u0128\7g\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("\u012a\7w\2\2\u012a\u012b\7t\2\2\u012b\u012c\7p\2\2\u012c")
        buf.write("\64\3\2\2\2\u012d\u012e\7x\2\2\u012e\u012f\7q\2\2\u012f")
        buf.write("\u0130\7k\2\2\u0130\u0131\7f\2\2\u0131\66\3\2\2\2\u0132")
        buf.write("\u0133\7v\2\2\u0133\u0134\7t\2\2\u0134\u0135\7w\2\2\u0135")
        buf.write("\u0136\7g\2\2\u01368\3\2\2\2\u0137\u0138\7h\2\2\u0138")
        buf.write("\u0139\7c\2\2\u0139\u013a\7n\2\2\u013a\u013b\7u\2\2\u013b")
        buf.write("\u013c\7g\2\2\u013c:\3\2\2\2\u013d\u013e\7p\2\2\u013e")
        buf.write("\u013f\7k\2\2\u013f\u0140\7n\2\2\u0140<\3\2\2\2\u0141")
        buf.write("\u0142\7v\2\2\u0142\u0143\7j\2\2\u0143\u0144\7k\2\2\u0144")
        buf.write("\u0145\7u\2\2\u0145>\3\2\2\2\u0146\u0147\7h\2\2\u0147")
        buf.write("\u0148\7k\2\2\u0148\u0149\7p\2\2\u0149\u014a\7c\2\2\u014a")
        buf.write("\u014b\7n\2\2\u014b@\3\2\2\2\u014c\u014d\7u\2\2\u014d")
        buf.write("\u014e\7v\2\2\u014e\u014f\7c\2\2\u014f\u0150\7v\2\2\u0150")
        buf.write("\u0151\7k\2\2\u0151\u0152\7e\2\2\u0152B\3\2\2\2\u0153")
        buf.write("\u0154\7v\2\2\u0154\u0155\7q\2\2\u0155D\3\2\2\2\u0156")
        buf.write("\u0157\7f\2\2\u0157\u0158\7q\2\2\u0158\u0159\7y\2\2\u0159")
        buf.write("\u015a\7p\2\2\u015a\u015b\7v\2\2\u015b\u015c\7q\2\2\u015c")
        buf.write("F\3\2\2\2\u015d\u015e\7-\2\2\u015eH\3\2\2\2\u015f\u0160")
        buf.write("\7/\2\2\u0160J\3\2\2\2\u0161\u0162\7,\2\2\u0162L\3\2\2")
        buf.write("\2\u0163\u0164\7\61\2\2\u0164N\3\2\2\2\u0165\u0166\7^")
        buf.write("\2\2\u0166P\3\2\2\2\u0167\u0168\7\'\2\2\u0168R\3\2\2\2")
        buf.write("\u0169\u016a\7#\2\2\u016a\u016b\7?\2\2\u016bT\3\2\2\2")
        buf.write("\u016c\u016d\7?\2\2\u016d\u016e\7?\2\2\u016eV\3\2\2\2")
        buf.write("\u016f\u0170\7>\2\2\u0170X\3\2\2\2\u0171\u0172\7@\2\2")
        buf.write("\u0172Z\3\2\2\2\u0173\u0174\7>\2\2\u0174\u0175\7?\2\2")
        buf.write("\u0175\\\3\2\2\2\u0176\u0177\7@\2\2\u0177\u0178\7?\2\2")
        buf.write("\u0178^\3\2\2\2\u0179\u017a\7~\2\2\u017a\u017b\7~\2\2")
        buf.write("\u017b`\3\2\2\2\u017c\u017d\7(\2\2\u017d\u017e\7(\2\2")
        buf.write("\u017eb\3\2\2\2\u017f\u0180\7#\2\2\u0180d\3\2\2\2\u0181")
        buf.write("\u0182\7`\2\2\u0182f\3\2\2\2\u0183\u0184\7*\2\2\u0184")
        buf.write("h\3\2\2\2\u0185\u0186\7+\2\2\u0186j\3\2\2\2\u0187\u0188")
        buf.write("\7}\2\2\u0188l\3\2\2\2\u0189\u018a\7\177\2\2\u018an\3")
        buf.write("\2\2\2\u018b\u018c\7.\2\2\u018cp\3\2\2\2\u018d\u018e\7")
        buf.write("]\2\2\u018er\3\2\2\2\u018f\u0190\7_\2\2\u0190t\3\2\2\2")
        buf.write("\u0191\u0192\7\60\2\2\u0192v\3\2\2\2\u0193\u0194\7=\2")
        buf.write("\2\u0194x\3\2\2\2\u0195\u0196\7<\2\2\u0196z\3\2\2\2\u0197")
        buf.write("\u0198\7<\2\2\u0198\u0199\7?\2\2\u0199|\3\2\2\2\u019a")
        buf.write("\u019e\t\7\2\2\u019b\u019d\t\b\2\2\u019c\u019b\3\2\2\2")
        buf.write("\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f~\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2")
        buf.write("\7\61\2\2\u01a2\u01a3\7,\2\2\u01a3\u01a7\3\2\2\2\u01a4")
        buf.write("\u01a6\13\2\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2")
        buf.write("\2\u01a7\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01aa")
        buf.write("\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\7,\2\2\u01ab")
        buf.write("\u01ac\7\61\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ae\b@\2\2")
        buf.write("\u01ae\u0080\3\2\2\2\u01af\u01b3\7%\2\2\u01b0\u01b2\n")
        buf.write("\t\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b6\u01b7\bA\2\2\u01b7\u0082\3\2\2\2")
        buf.write("\u01b8\u01ba\t\n\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3")
        buf.write("\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u01be\bB\2\2\u01be\u0084\3\2\2\2\u01bf")
        buf.write("\u01c3\7$\2\2\u01c0\u01c2\5\23\n\2\u01c1\u01c0\3\2\2\2")
        buf.write("\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4\u01ca\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c8")
        buf.write("\7\2\2\3\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8")
        buf.write("\u01cb\3\2\2\2\u01c9\u01cb\n\13\2\2\u01ca\u01c7\3\2\2")
        buf.write("\2\u01ca\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd")
        buf.write("\bC\3\2\u01cd\u0086\3\2\2\2\u01ce\u01d2\7$\2\2\u01cf\u01d1")
        buf.write("\5\23\n\2\u01d0\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5\3\2\2\2")
        buf.write("\u01d4\u01d2\3\2\2\2\u01d5\u01d6\7^\2\2\u01d6\u01d7\n")
        buf.write("\6\2\2\u01d7\u01d8\bD\4\2\u01d8\u0088\3\2\2\2\u01d9\u01da")
        buf.write("\13\2\2\2\u01da\u01db\bE\5\2\u01db\u008a\3\2\2\2\26\2")
        buf.write("\u0090\u0095\u0098\u009d\u00a3\u00a8\u00ad\u00b1\u00b7")
        buf.write("\u00bf\u00d6\u019e\u01a7\u01b3\u01bb\u01c3\u01c7\u01ca")
        buf.write("\u01d2\6\b\2\2\3C\2\3D\3\3E\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTLIT = 2
    FLOATLIT = 3
    BOOLIT = 4
    STRINGLIT = 5
    WRITELN = 6
    BOOLEAN = 7
    BREAK = 8
    CLASS = 9
    CONTINUE = 10
    DO = 11
    ELSE = 12
    EXTENDS = 13
    FLOATTYPE = 14
    IF = 15
    INTTYPE = 16
    NEW = 17
    STRING = 18
    THEN = 19
    FOR = 20
    RETURN = 21
    VOIDTYPE = 22
    TRUE = 23
    FALSE = 24
    NIL = 25
    THIS = 26
    FINAL = 27
    STATIC = 28
    TO = 29
    DOWNTO = 30
    ADD = 31
    SUB = 32
    MUL = 33
    FLOAT_DIV = 34
    INT_DIV = 35
    MOD = 36
    NOT_EQ = 37
    EQ = 38
    LT = 39
    GT = 40
    LT_EQ = 41
    GT_EQ = 42
    OR = 43
    AND = 44
    NOT = 45
    CONCAT = 46
    LB = 47
    RB = 48
    LP = 49
    RP = 50
    COMMA = 51
    LSQB = 52
    RSQB = 53
    DOT = 54
    SEMI = 55
    COLON = 56
    ASS = 57
    ID = 58
    BLOCK_COMMENT = 59
    LINE_COMMENT = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'boolean'", "'break'", "'class'", "'continue'", "'do'", 
            "'else'", "'extends'", "'float'", "'if'", "'int'", "'new'", 
            "'string'", "'then'", "'for'", "'return'", "'void'", "'true'", 
            "'false'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
            "'^'", "'('", "')'", "'{'", "'}'", "','", "'['", "']'", "'.'", 
            "';'", "':'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLIT", "STRINGLIT", "WRITELN", "BOOLEAN", 
            "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOATTYPE", 
            "IF", "INTTYPE", "NEW", "STRING", "THEN", "FOR", "RETURN", "VOIDTYPE", 
            "TRUE", "FALSE", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
            "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", "NOT_EQ", 
            "EQ", "LT", "GT", "LT_EQ", "GT_EQ", "OR", "AND", "NOT", "CONCAT", 
            "LB", "RB", "LP", "RP", "COMMA", "LSQB", "RSQB", "DOT", "SEMI", 
            "COLON", "ASS", "ID", "BLOCK_COMMENT", "LINE_COMMENT", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "INTLIT", "FLOATLIT", "INTPART", "DECIPART", "EXPPART", 
                  "BOOLIT", "STRINGLIT", "CHAR", "WRITELN", "BOOLEAN", "BREAK", 
                  "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOATTYPE", 
                  "IF", "INTTYPE", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                  "VOIDTYPE", "TRUE", "FALSE", "NIL", "THIS", "FINAL", "STATIC", 
                  "TO", "DOWNTO", "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", 
                  "MOD", "NOT_EQ", "EQ", "LT", "GT", "LT_EQ", "GT_EQ", "OR", 
                  "AND", "NOT", "CONCAT", "LB", "RB", "LP", "RP", "COMMA", 
                  "LSQB", "RSQB", "DOT", "SEMI", "COLON", "ASS", "ID", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	if self.text[-1] in ['\r','\n']:
            		raise UncloseString(self.text[0:-1])
            	else: raise UncloseString(self.text[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	raise IllegalEscape(self.text[0:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


