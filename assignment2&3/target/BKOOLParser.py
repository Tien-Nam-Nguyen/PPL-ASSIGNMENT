# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01be\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3h\n\3\3")
        buf.write("\4\3\4\3\4\3\4\5\4n\n\4\3\4\3\4\5\4r\n\4\3\4\3\4\3\5\3")
        buf.write("\5\6\5x\n\5\r\5\16\5y\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0082")
        buf.write("\n\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u008d\n\7")
        buf.write("\3\b\3\b\3\b\5\b\u0092\n\b\3\t\5\t\u0095\n\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u009b\n\t\3\t\3\t\3\t\3\t\5\t\u00a1\n\t\3\n")
        buf.write("\3\n\3\n\5\n\u00a6\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00b0\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00b9\n\r\3\16\3\16\5\16\u00bd\n\16\3\16\5\16\u00c0\n")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u00c8\n\17\3\20")
        buf.write("\5\20\u00cb\n\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\5")
        buf.write("\21\u00d4\n\21\3\21\3\21\3\21\3\21\3\21\5\21\u00db\n\21")
        buf.write("\5\21\u00dd\n\21\3\22\3\22\3\22\3\22\5\22\u00e3\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ed\n\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\5\25\u00f6\n\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\5\26\u00fe\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0118\n\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u0123\n\34\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u012a\n\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0132\n")
        buf.write("\36\f\36\16\36\u0135\13\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\7\37\u013d\n\37\f\37\16\37\u0140\13\37\3 \3 \3 \3")
        buf.write(" \3 \3 \7 \u0148\n \f \16 \u014b\13 \3!\3!\3!\3!\3!\3")
        buf.write("!\7!\u0153\n!\f!\16!\u0156\13!\3\"\3\"\3\"\5\"\u015b\n")
        buf.write("\"\3#\3#\3#\5#\u0160\n#\3$\3$\3$\3$\3$\3$\5$\u0168\n$")
        buf.write("\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0175\n%\3%\7%\u0178")
        buf.write("\n%\f%\16%\u017b\13%\3&\3&\3&\3&\5&\u0181\n&\3&\3&\5&")
        buf.write("\u0185\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0190")
        buf.write("\n\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\5)\u019b\n)\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3+\5+\u01a7\n+\3,\3,\5,\u01ab\n,\3-\3")
        buf.write("-\5-\u01af\n-\3.\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\5\60\u01bc\n\60\3\60\2\7:<>@H\61\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^\2\n\3\2\37 \3\2),\3\2\'(\3\2-.\3\2!\"\3\2#")
        buf.write("&\7\2\t\t\20\20\22\22\24\24<<\3\2\4\7\2\u01cf\2`\3\2\2")
        buf.write("\2\4g\3\2\2\2\6i\3\2\2\2\bw\3\2\2\2\n\u0081\3\2\2\2\f")
        buf.write("\u008c\3\2\2\2\16\u008e\3\2\2\2\20\u00a0\3\2\2\2\22\u00a2")
        buf.write("\3\2\2\2\24\u00af\3\2\2\2\26\u00b1\3\2\2\2\30\u00b8\3")
        buf.write("\2\2\2\32\u00ba\3\2\2\2\34\u00c7\3\2\2\2\36\u00ca\3\2")
        buf.write("\2\2 \u00dc\3\2\2\2\"\u00e2\3\2\2\2$\u00ec\3\2\2\2&\u00ee")
        buf.write("\3\2\2\2(\u00f5\3\2\2\2*\u00f7\3\2\2\2,\u00ff\3\2\2\2")
        buf.write(".\u0108\3\2\2\2\60\u010b\3\2\2\2\62\u010e\3\2\2\2\64\u0112")
        buf.write("\3\2\2\2\66\u0122\3\2\2\28\u0129\3\2\2\2:\u012b\3\2\2")
        buf.write("\2<\u0136\3\2\2\2>\u0141\3\2\2\2@\u014c\3\2\2\2B\u015a")
        buf.write("\3\2\2\2D\u015f\3\2\2\2F\u0167\3\2\2\2H\u0169\3\2\2\2")
        buf.write("J\u0184\3\2\2\2L\u018f\3\2\2\2N\u0191\3\2\2\2P\u019a\3")
        buf.write("\2\2\2R\u019c\3\2\2\2T\u01a6\3\2\2\2V\u01aa\3\2\2\2X\u01ae")
        buf.write("\3\2\2\2Z\u01b0\3\2\2\2\\\u01b4\3\2\2\2^\u01bb\3\2\2\2")
        buf.write("`a\5\4\3\2ab\7\2\2\3b\3\3\2\2\2cd\5\6\4\2de\5\4\3\2eh")
        buf.write("\3\2\2\2fh\5\6\4\2gc\3\2\2\2gf\3\2\2\2h\5\3\2\2\2ij\7")
        buf.write("\13\2\2jm\7<\2\2kl\7\17\2\2ln\7<\2\2mk\3\2\2\2mn\3\2\2")
        buf.write("\2no\3\2\2\2oq\7\63\2\2pr\5\b\5\2qp\3\2\2\2qr\3\2\2\2")
        buf.write("rs\3\2\2\2st\7\64\2\2t\7\3\2\2\2ux\5\n\6\2vx\5\20\t\2")
        buf.write("wu\3\2\2\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\t")
        buf.write("\3\2\2\2{\u0082\7\35\2\2|\u0082\7\36\2\2}~\7\36\2\2~\u0082")
        buf.write("\7\35\2\2\177\u0080\7\35\2\2\u0080\u0082\7\36\2\2\u0081")
        buf.write("{\3\2\2\2\u0081|\3\2\2\2\u0081}\3\2\2\2\u0081\177\3\2")
        buf.write("\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\5V,\2\u0084\u0085\5\f\7\2\u0085\u0086\79\2\2\u0086\13")
        buf.write("\3\2\2\2\u0087\u0088\5\16\b\2\u0088\u0089\7\65\2\2\u0089")
        buf.write("\u008a\5\f\7\2\u008a\u008d\3\2\2\2\u008b\u008d\5\16\b")
        buf.write("\2\u008c\u0087\3\2\2\2\u008c\u008b\3\2\2\2\u008d\r\3\2")
        buf.write("\2\2\u008e\u0091\7<\2\2\u008f\u0090\7\3\2\2\u0090\u0092")
        buf.write("\5\66\34\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\17\3\2\2\2\u0093\u0095\7\36\2\2\u0094\u0093\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\5X-\2\u0097")
        buf.write("\u0098\7<\2\2\u0098\u009a\7\61\2\2\u0099\u009b\5\24\13")
        buf.write("\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009d\7\62\2\2\u009d\u009e\5\32\16\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u00a1\5\22\n\2\u00a0\u0094\3\2\2")
        buf.write("\2\u00a0\u009f\3\2\2\2\u00a1\21\3\2\2\2\u00a2\u00a3\7")
        buf.write("<\2\2\u00a3\u00a5\7\61\2\2\u00a4\u00a6\5\24\13\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00a8\7\62\2\2\u00a8\u00a9\5\32\16\2\u00a9\23\3")
        buf.write("\2\2\2\u00aa\u00ab\5\26\f\2\u00ab\u00ac\79\2\2\u00ac\u00ad")
        buf.write("\5\24\13\2\u00ad\u00b0\3\2\2\2\u00ae\u00b0\5\26\f\2\u00af")
        buf.write("\u00aa\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\25\3\2\2\2\u00b1")
        buf.write("\u00b2\5V,\2\u00b2\u00b3\5\30\r\2\u00b3\27\3\2\2\2\u00b4")
        buf.write("\u00b5\7<\2\2\u00b5\u00b6\7\65\2\2\u00b6\u00b9\5\30\r")
        buf.write("\2\u00b7\u00b9\7<\2\2\u00b8\u00b4\3\2\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b9\31\3\2\2\2\u00ba\u00bc\7\63\2\2\u00bb\u00bd")
        buf.write("\5\34\17\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00bf\3\2\2\2\u00be\u00c0\5\"\22\2\u00bf\u00be\3\2\2")
        buf.write("\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2")
        buf.write("\7\64\2\2\u00c2\33\3\2\2\2\u00c3\u00c4\5\36\20\2\u00c4")
        buf.write("\u00c5\5\34\17\2\u00c5\u00c8\3\2\2\2\u00c6\u00c8\5\36")
        buf.write("\20\2\u00c7\u00c3\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\35")
        buf.write("\3\2\2\2\u00c9\u00cb\7\35\2\2\u00ca\u00c9\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\5V,\2\u00cd")
        buf.write("\u00ce\5 \21\2\u00ce\u00cf\79\2\2\u00cf\37\3\2\2\2\u00d0")
        buf.write("\u00d3\7<\2\2\u00d1\u00d2\7\3\2\2\u00d2\u00d4\5\66\34")
        buf.write("\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\u00d6\7\65\2\2\u00d6\u00dd\5 \21\2\u00d7")
        buf.write("\u00da\7<\2\2\u00d8\u00d9\7\3\2\2\u00d9\u00db\5\66\34")
        buf.write("\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dd")
        buf.write("\3\2\2\2\u00dc\u00d0\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dd")
        buf.write("!\3\2\2\2\u00de\u00df\5$\23\2\u00df\u00e0\5\"\22\2\u00e0")
        buf.write("\u00e3\3\2\2\2\u00e1\u00e3\5$\23\2\u00e2\u00de\3\2\2\2")
        buf.write("\u00e2\u00e1\3\2\2\2\u00e3#\3\2\2\2\u00e4\u00ed\5\32\16")
        buf.write("\2\u00e5\u00ed\5&\24\2\u00e6\u00ed\5*\26\2\u00e7\u00ed")
        buf.write("\5,\27\2\u00e8\u00ed\5.\30\2\u00e9\u00ed\5\60\31\2\u00ea")
        buf.write("\u00ed\5\62\32\2\u00eb\u00ed\5\64\33\2\u00ec\u00e4\3\2")
        buf.write("\2\2\u00ec\u00e5\3\2\2\2\u00ec\u00e6\3\2\2\2\u00ec\u00e7")
        buf.write("\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed%\3\2\2\2\u00ee")
        buf.write("\u00ef\5(\25\2\u00ef\u00f0\7;\2\2\u00f0\u00f1\5\66\34")
        buf.write("\2\u00f1\u00f2\79\2\2\u00f2\'\3\2\2\2\u00f3\u00f6\7<\2")
        buf.write("\2\u00f4\u00f6\5F$\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3")
        buf.write("\2\2\2\u00f6)\3\2\2\2\u00f7\u00f8\7\21\2\2\u00f8\u00f9")
        buf.write("\5\66\34\2\u00f9\u00fa\7\25\2\2\u00fa\u00fd\5$\23\2\u00fb")
        buf.write("\u00fc\7\16\2\2\u00fc\u00fe\5$\23\2\u00fd\u00fb\3\2\2")
        buf.write("\2\u00fd\u00fe\3\2\2\2\u00fe+\3\2\2\2\u00ff\u0100\7\26")
        buf.write("\2\2\u0100\u0101\7<\2\2\u0101\u0102\7;\2\2\u0102\u0103")
        buf.write("\5\66\34\2\u0103\u0104\t\2\2\2\u0104\u0105\5\66\34\2\u0105")
        buf.write("\u0106\7\r\2\2\u0106\u0107\5$\23\2\u0107-\3\2\2\2\u0108")
        buf.write("\u0109\7\n\2\2\u0109\u010a\79\2\2\u010a/\3\2\2\2\u010b")
        buf.write("\u010c\7\f\2\2\u010c\u010d\79\2\2\u010d\61\3\2\2\2\u010e")
        buf.write("\u010f\7\27\2\2\u010f\u0110\5\66\34\2\u0110\u0111\79\2")
        buf.write("\2\u0111\63\3\2\2\2\u0112\u0113\5H%\2\u0113\u0114\78\2")
        buf.write("\2\u0114\u0115\7<\2\2\u0115\u0117\7\61\2\2\u0116\u0118")
        buf.write("\5P)\2\u0117\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119")
        buf.write("\3\2\2\2\u0119\u011a\7\62\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("\u011c\79\2\2\u011c\65\3\2\2\2\u011d\u011e\58\35\2\u011e")
        buf.write("\u011f\t\3\2\2\u011f\u0120\58\35\2\u0120\u0123\3\2\2\2")
        buf.write("\u0121\u0123\58\35\2\u0122\u011d\3\2\2\2\u0122\u0121\3")
        buf.write("\2\2\2\u0123\67\3\2\2\2\u0124\u0125\5:\36\2\u0125\u0126")
        buf.write("\t\4\2\2\u0126\u0127\5:\36\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u012a\5:\36\2\u0129\u0124\3\2\2\2\u0129\u0128\3\2\2\2")
        buf.write("\u012a9\3\2\2\2\u012b\u012c\b\36\1\2\u012c\u012d\5<\37")
        buf.write("\2\u012d\u0133\3\2\2\2\u012e\u012f\f\4\2\2\u012f\u0130")
        buf.write("\t\5\2\2\u0130\u0132\5<\37\2\u0131\u012e\3\2\2\2\u0132")
        buf.write("\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134;\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0137\b\37\1")
        buf.write("\2\u0137\u0138\5> \2\u0138\u013e\3\2\2\2\u0139\u013a\f")
        buf.write("\4\2\2\u013a\u013b\t\6\2\2\u013b\u013d\5> \2\u013c\u0139")
        buf.write("\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013f=\3\2\2\2\u0140\u013e\3\2\2\2\u0141")
        buf.write("\u0142\b \1\2\u0142\u0143\5@!\2\u0143\u0149\3\2\2\2\u0144")
        buf.write("\u0145\f\4\2\2\u0145\u0146\t\7\2\2\u0146\u0148\5@!\2\u0147")
        buf.write("\u0144\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a?\3\2\2\2\u014b\u0149\3\2\2")
        buf.write("\2\u014c\u014d\b!\1\2\u014d\u014e\5B\"\2\u014e\u0154\3")
        buf.write("\2\2\2\u014f\u0150\f\4\2\2\u0150\u0151\7\60\2\2\u0151")
        buf.write("\u0153\5B\"\2\u0152\u014f\3\2\2\2\u0153\u0156\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155A\3\2\2")
        buf.write("\2\u0156\u0154\3\2\2\2\u0157\u0158\7/\2\2\u0158\u015b")
        buf.write("\5B\"\2\u0159\u015b\5D#\2\u015a\u0157\3\2\2\2\u015a\u0159")
        buf.write("\3\2\2\2\u015bC\3\2\2\2\u015c\u015d\t\6\2\2\u015d\u0160")
        buf.write("\5D#\2\u015e\u0160\5F$\2\u015f\u015c\3\2\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160E\3\2\2\2\u0161\u0162\5H%\2\u0162\u0163")
        buf.write("\7\66\2\2\u0163\u0164\5\66\34\2\u0164\u0165\7\67\2\2\u0165")
        buf.write("\u0168\3\2\2\2\u0166\u0168\5H%\2\u0167\u0161\3\2\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0168G\3\2\2\2\u0169\u016a\b%\1\2\u016a")
        buf.write("\u016b\5J&\2\u016b\u0179\3\2\2\2\u016c\u016d\f\5\2\2\u016d")
        buf.write("\u016e\78\2\2\u016e\u0178\7<\2\2\u016f\u0170\f\4\2\2\u0170")
        buf.write("\u0171\78\2\2\u0171\u0172\7<\2\2\u0172\u0174\7\61\2\2")
        buf.write("\u0173\u0175\5P)\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2")
        buf.write("\2\2\u0175\u0176\3\2\2\2\u0176\u0178\7\62\2\2\u0177\u016c")
        buf.write("\3\2\2\2\u0177\u016f\3\2\2\2\u0178\u017b\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017aI\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017c\u017d\7\23\2\2\u017d\u017e\7<\2\2")
        buf.write("\u017e\u0180\7\61\2\2\u017f\u0181\5P)\2\u0180\u017f\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0185")
        buf.write("\7\62\2\2\u0183\u0185\5L\'\2\u0184\u017c\3\2\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185K\3\2\2\2\u0186\u0190\7<\2\2\u0187")
        buf.write("\u0190\7\4\2\2\u0188\u0190\7\5\2\2\u0189\u0190\7\7\2\2")
        buf.write("\u018a\u0190\7\6\2\2\u018b\u0190\7\33\2\2\u018c\u0190")
        buf.write("\5N(\2\u018d\u0190\7\34\2\2\u018e\u0190\5Z.\2\u018f\u0186")
        buf.write("\3\2\2\2\u018f\u0187\3\2\2\2\u018f\u0188\3\2\2\2\u018f")
        buf.write("\u0189\3\2\2\2\u018f\u018a\3\2\2\2\u018f\u018b\3\2\2\2")
        buf.write("\u018f\u018c\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u018e\3")
        buf.write("\2\2\2\u0190M\3\2\2\2\u0191\u0192\7\61\2\2\u0192\u0193")
        buf.write("\5\66\34\2\u0193\u0194\7\62\2\2\u0194O\3\2\2\2\u0195\u0196")
        buf.write("\5\66\34\2\u0196\u0197\7\65\2\2\u0197\u0198\5P)\2\u0198")
        buf.write("\u019b\3\2\2\2\u0199\u019b\5\66\34\2\u019a\u0195\3\2\2")
        buf.write("\2\u019a\u0199\3\2\2\2\u019bQ\3\2\2\2\u019c\u019d\t\b")
        buf.write("\2\2\u019d\u019e\7\66\2\2\u019e\u019f\7\4\2\2\u019f\u01a0")
        buf.write("\7\67\2\2\u01a0S\3\2\2\2\u01a1\u01a7\7\22\2\2\u01a2\u01a7")
        buf.write("\7\20\2\2\u01a3\u01a7\7\24\2\2\u01a4\u01a7\7\t\2\2\u01a5")
        buf.write("\u01a7\5R*\2\u01a6\u01a1\3\2\2\2\u01a6\u01a2\3\2\2\2\u01a6")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2")
        buf.write("\u01a7U\3\2\2\2\u01a8\u01ab\5T+\2\u01a9\u01ab\7<\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abW\3\2\2\2\u01ac")
        buf.write("\u01af\5V,\2\u01ad\u01af\7\30\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01ad\3\2\2\2\u01afY\3\2\2\2\u01b0\u01b1\7\63\2")
        buf.write("\2\u01b1\u01b2\5^\60\2\u01b2\u01b3\7\64\2\2\u01b3[\3\2")
        buf.write("\2\2\u01b4\u01b5\t\t\2\2\u01b5]\3\2\2\2\u01b6\u01b7\5")
        buf.write("\\/\2\u01b7\u01b8\7\65\2\2\u01b8\u01b9\5^\60\2\u01b9\u01bc")
        buf.write("\3\2\2\2\u01ba\u01bc\5\\/\2\u01bb\u01b6\3\2\2\2\u01bb")
        buf.write("\u01ba\3\2\2\2\u01bc_\3\2\2\2\60gmqwy\u0081\u008c\u0091")
        buf.write("\u0094\u009a\u00a0\u00a5\u00af\u00b8\u00bc\u00bf\u00c7")
        buf.write("\u00ca\u00d3\u00da\u00dc\u00e2\u00ec\u00f5\u00fd\u0117")
        buf.write("\u0122\u0129\u0133\u013e\u0149\u0154\u015a\u015f\u0167")
        buf.write("\u0174\u0177\u0179\u0180\u0184\u018f\u019a\u01a6\u01aa")
        buf.write("\u01ae\u01bb")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'boolean'", "'break'", "'class'", 
                     "'continue'", "'do'", "'else'", "'extends'", "'float'", 
                     "'if'", "'int'", "'new'", "'string'", "'then'", "'for'", 
                     "'return'", "'void'", "'true'", "'false'", "'nil'", 
                     "'this'", "'final'", "'static'", "'to'", "'downto'", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'^'", "'('", "')'", "'{'", "'}'", "','", "'['", 
                     "']'", "'.'", "';'", "':'", "':='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTLIT", "FLOATLIT", "BOOLIT", 
                      "STRINGLIT", "WRITELN", "BOOLEAN", "BREAK", "CLASS", 
                      "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOATTYPE", 
                      "IF", "INTTYPE", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                      "VOIDTYPE", "TRUE", "FALSE", "NIL", "THIS", "FINAL", 
                      "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", "FLOAT_DIV", 
                      "INT_DIV", "MOD", "NOT_EQ", "EQ", "LT", "GT", "LT_EQ", 
                      "GT_EQ", "OR", "AND", "NOT", "CONCAT", "LB", "RB", 
                      "LP", "RP", "COMMA", "LSQB", "RSQB", "DOT", "SEMI", 
                      "COLON", "ASS", "ID", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classDecls = 1
    RULE_classDecl = 2
    RULE_memberListNoNull = 3
    RULE_classAttr = 4
    RULE_attrDecls = 5
    RULE_attrDecl = 6
    RULE_classMethod = 7
    RULE_constructor = 8
    RULE_params = 9
    RULE_param = 10
    RULE_ids = 11
    RULE_blockStmt = 12
    RULE_varDecls = 13
    RULE_varDecl = 14
    RULE_listVar = 15
    RULE_stmts = 16
    RULE_stmt = 17
    RULE_assignStmt = 18
    RULE_lhs = 19
    RULE_ifStmt = 20
    RULE_forStmt = 21
    RULE_breakStmt = 22
    RULE_contiStmt = 23
    RULE_returnStmt = 24
    RULE_invoStmt = 25
    RULE_expr = 26
    RULE_expr1 = 27
    RULE_expr2 = 28
    RULE_expr3 = 29
    RULE_expr4 = 30
    RULE_expr5 = 31
    RULE_expr6 = 32
    RULE_expr7 = 33
    RULE_expr8 = 34
    RULE_expr9 = 35
    RULE_expr10 = 36
    RULE_expr11 = 37
    RULE_sube = 38
    RULE_exprs = 39
    RULE_arraytype = 40
    RULE_ptype = 41
    RULE_typ = 42
    RULE_methodtype = 43
    RULE_arraylit = 44
    RULE_ele = 45
    RULE_ele_list = 46

    ruleNames =  [ "program", "classDecls", "classDecl", "memberListNoNull", 
                   "classAttr", "attrDecls", "attrDecl", "classMethod", 
                   "constructor", "params", "param", "ids", "blockStmt", 
                   "varDecls", "varDecl", "listVar", "stmts", "stmt", "assignStmt", 
                   "lhs", "ifStmt", "forStmt", "breakStmt", "contiStmt", 
                   "returnStmt", "invoStmt", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "expr11", "sube", "exprs", "arraytype", "ptype", 
                   "typ", "methodtype", "arraylit", "ele", "ele_list" ]

    EOF = Token.EOF
    T__0=1
    INTLIT=2
    FLOATLIT=3
    BOOLIT=4
    STRINGLIT=5
    WRITELN=6
    BOOLEAN=7
    BREAK=8
    CLASS=9
    CONTINUE=10
    DO=11
    ELSE=12
    EXTENDS=13
    FLOATTYPE=14
    IF=15
    INTTYPE=16
    NEW=17
    STRING=18
    THEN=19
    FOR=20
    RETURN=21
    VOIDTYPE=22
    TRUE=23
    FALSE=24
    NIL=25
    THIS=26
    FINAL=27
    STATIC=28
    TO=29
    DOWNTO=30
    ADD=31
    SUB=32
    MUL=33
    FLOAT_DIV=34
    INT_DIV=35
    MOD=36
    NOT_EQ=37
    EQ=38
    LT=39
    GT=40
    LT_EQ=41
    GT_EQ=42
    OR=43
    AND=44
    NOT=45
    CONCAT=46
    LB=47
    RB=48
    LP=49
    RP=50
    COMMA=51
    LSQB=52
    RSQB=53
    DOT=54
    SEMI=55
    COLON=56
    ASS=57
    ID=58
    BLOCK_COMMENT=59
    LINE_COMMENT=60
    WS=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecls(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.classDecls()
            self.state = 95
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclContext,0)


        def classDecls(self):
            return self.getTypedRuleContext(BKOOLParser.ClassDeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecls" ):
                return visitor.visitClassDecls(self)
            else:
                return visitor.visitChildren(self)




    def classDecls(self):

        localctx = BKOOLParser.ClassDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDecls)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.classDecl()
                self.state = 98
                self.classDecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.classDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def memberListNoNull(self):
            return self.getTypedRuleContext(BKOOLParser.MemberListNoNullContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(BKOOLParser.CLASS)
            self.state = 104
            self.match(BKOOLParser.ID)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 105
                self.match(BKOOLParser.EXTENDS)
                self.state = 106
                self.match(BKOOLParser.ID)


            self.state = 109
            self.match(BKOOLParser.LP)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOATTYPE) | (1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOIDTYPE) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 110
                self.memberListNoNull()


            self.state = 113
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberListNoNullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classAttr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassAttrContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassAttrContext,i)


        def classMethod(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassMethodContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassMethodContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memberListNoNull

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberListNoNull" ):
                return visitor.visitMemberListNoNull(self)
            else:
                return visitor.visitChildren(self)




    def memberListNoNull(self):

        localctx = BKOOLParser.MemberListNoNullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memberListNoNull)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 115
                    self.classAttr()
                    pass

                elif la_ == 2:
                    self.state = 116
                    self.classMethod()
                    pass


                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOATTYPE) | (1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOIDTYPE) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def attrDecls(self):
            return self.getTypedRuleContext(BKOOLParser.AttrDeclsContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classAttr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassAttr" ):
                return visitor.visitClassAttr(self)
            else:
                return visitor.visitChildren(self)




    def classAttr(self):

        localctx = BKOOLParser.ClassAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classAttr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 121
                self.match(BKOOLParser.FINAL)

            elif la_ == 2:
                self.state = 122
                self.match(BKOOLParser.STATIC)

            elif la_ == 3:
                self.state = 123
                self.match(BKOOLParser.STATIC)
                self.state = 124
                self.match(BKOOLParser.FINAL)

            elif la_ == 4:
                self.state = 125
                self.match(BKOOLParser.FINAL)
                self.state = 126
                self.match(BKOOLParser.STATIC)


            self.state = 129
            self.typ()
            self.state = 130
            self.attrDecls()
            self.state = 131
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrDecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttrDeclContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attrDecls(self):
            return self.getTypedRuleContext(BKOOLParser.AttrDeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrDecls" ):
                return visitor.visitAttrDecls(self)
            else:
                return visitor.visitChildren(self)




    def attrDecls(self):

        localctx = BKOOLParser.AttrDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrDecls)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.attrDecl()
                self.state = 134
                self.match(BKOOLParser.COMMA)
                self.state = 135
                self.attrDecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.attrDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrDecl" ):
                return visitor.visitAttrDecl(self)
            else:
                return visitor.visitChildren(self)




    def attrDecl(self):

        localctx = BKOOLParser.AttrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(BKOOLParser.ID)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.T__0:
                self.state = 141
                self.match(BKOOLParser.T__0)
                self.state = 142
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodtype(self):
            return self.getTypedRuleContext(BKOOLParser.MethodtypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMethod" ):
                return visitor.visitClassMethod(self)
            else:
                return visitor.visitChildren(self)




    def classMethod(self):

        localctx = BKOOLParser.ClassMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_classMethod)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 145
                    self.match(BKOOLParser.STATIC)


                self.state = 148
                self.methodtype()
                self.state = 149
                self.match(BKOOLParser.ID)
                self.state = 150
                self.match(BKOOLParser.LB)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOATTYPE) | (1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 151
                    self.params()


                self.state = 154
                self.match(BKOOLParser.RB)
                self.state = 155
                self.blockStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(BKOOLParser.ID)
            self.state = 161
            self.match(BKOOLParser.LB)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOATTYPE) | (1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 162
                self.params()


            self.state = 165
            self.match(BKOOLParser.RB)
            self.state = 166
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_params)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.param()
                self.state = 169
                self.match(BKOOLParser.SEMI)
                self.state = 170
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ids(self):
            return self.getTypedRuleContext(BKOOLParser.IdsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.typ()
            self.state = 176
            self.ids()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def ids(self):
            return self.getTypedRuleContext(BKOOLParser.IdsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = BKOOLParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ids)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(BKOOLParser.ID)
                self.state = 179
                self.match(BKOOLParser.COMMA)
                self.state = 180
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def varDecls(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclsContext,0)


        def stmts(self):
            return self.getTypedRuleContext(BKOOLParser.StmtsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = BKOOLParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BKOOLParser.LP)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 185
                self.varDecls()


            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 188
                self.stmts()


            self.state = 191
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclContext,0)


        def varDecls(self):
            return self.getTypedRuleContext(BKOOLParser.VarDeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_varDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecls" ):
                return visitor.visitVarDecls(self)
            else:
                return visitor.visitChildren(self)




    def varDecls(self):

        localctx = BKOOLParser.VarDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varDecls)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.varDecl()
                self.state = 194
                self.varDecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.varDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def listVar(self):
            return self.getTypedRuleContext(BKOOLParser.ListVarContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = BKOOLParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 199
                self.match(BKOOLParser.FINAL)


            self.state = 202
            self.typ()
            self.state = 203
            self.listVar()
            self.state = 204
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def listVar(self):
            return self.getTypedRuleContext(BKOOLParser.ListVarContext,0)


        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListVar" ):
                return visitor.visitListVar(self)
            else:
                return visitor.visitChildren(self)




    def listVar(self):

        localctx = BKOOLParser.ListVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listVar)
        self._la = 0 # Token type
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(BKOOLParser.ID)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.T__0:
                    self.state = 207
                    self.match(BKOOLParser.T__0)
                    self.state = 208
                    self.expr()


                self.state = 211
                self.match(BKOOLParser.COMMA)
                self.state = 212
                self.listVar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(BKOOLParser.ID)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.T__0:
                    self.state = 214
                    self.match(BKOOLParser.T__0)
                    self.state = 215
                    self.expr()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmts(self):
            return self.getTypedRuleContext(BKOOLParser.StmtsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = BKOOLParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmts)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.stmt()
                self.state = 221
                self.stmts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def contiStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContiStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStmtContext,0)


        def invoStmt(self):
            return self.getTypedRuleContext(BKOOLParser.InvoStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.blockStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.breakStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 231
                self.contiStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 232
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 233
                self.invoStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASS(self):
            return self.getToken(BKOOLParser.ASS, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = BKOOLParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.lhs()
            self.state = 237
            self.match(BKOOLParser.ASS)
            self.state = 238
            self.expr()
            self.state = 239
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lhs)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(BKOOLParser.IF)
            self.state = 246
            self.expr()
            self.state = 247
            self.match(BKOOLParser.THEN)
            self.state = 248
            self.stmt()
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 249
                self.match(BKOOLParser.ELSE)
                self.state = 250
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASS(self):
            return self.getToken(BKOOLParser.ASS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(BKOOLParser.FOR)
            self.state = 254
            self.match(BKOOLParser.ID)
            self.state = 255
            self.match(BKOOLParser.ASS)
            self.state = 256
            self.expr()
            self.state = 257
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 258
            self.expr()
            self.state = 259
            self.match(BKOOLParser.DO)
            self.state = 260
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(BKOOLParser.BREAK)
            self.state = 263
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContiStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_contiStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContiStmt" ):
                return visitor.visitContiStmt(self)
            else:
                return visitor.visitChildren(self)




    def contiStmt(self):

        localctx = BKOOLParser.ContiStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_contiStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(BKOOLParser.CONTINUE)
            self.state = 266
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(BKOOLParser.RETURN)
            self.state = 269
            self.expr()
            self.state = 270
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprs(self):
            return self.getTypedRuleContext(BKOOLParser.ExprsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_invoStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvoStmt" ):
                return visitor.visitInvoStmt(self)
            else:
                return visitor.visitChildren(self)




    def invoStmt(self):

        localctx = BKOOLParser.InvoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_invoStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.expr9(0)
            self.state = 273
            self.match(BKOOLParser.DOT)
            self.state = 274
            self.match(BKOOLParser.ID)
            self.state = 275
            self.match(BKOOLParser.LB)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 276
                self.exprs()


            self.state = 279
            self.match(BKOOLParser.RB)
            self.state = 281
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT_EQ(self):
            return self.getToken(BKOOLParser.GT_EQ, 0)

        def LT_EQ(self):
            return self.getToken(BKOOLParser.LT_EQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.expr1()
                self.state = 284
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LT_EQ) | (1 << BKOOLParser.GT_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 285
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NOT_EQ(self):
            return self.getToken(BKOOLParser.NOT_EQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.expr2(0)
                self.state = 291
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 292
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 300
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 301
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 302
                    self.expr3(0) 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 313
                    self.expr4(0) 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def INT_DIV(self):
            return self.getToken(BKOOLParser.INT_DIV, 0)

        def FLOAT_DIV(self):
            return self.getToken(BKOOLParser.FLOAT_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 322
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 323
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 324
                    self.expr5(0) 
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 333
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 334
                    self.match(BKOOLParser.CONCAT)
                    self.state = 335
                    self.expr6() 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr6)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(BKOOLParser.NOT)
                self.state = 342
                self.expr6()
                pass
            elif token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 347
                self.expr7()
                pass
            elif token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.expr8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def LSQB(self):
            return self.getToken(BKOOLParser.LSQB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSQB(self):
            return self.getToken(BKOOLParser.RSQB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = BKOOLParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr8)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.expr9(0)
                self.state = 352
                self.match(BKOOLParser.LSQB)
                self.state = 353
                self.expr()
                self.state = 354
                self.match(BKOOLParser.RSQB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.expr9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprs(self):
            return self.getTypedRuleContext(BKOOLParser.ExprsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 373
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 362
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 363
                        self.match(BKOOLParser.DOT)
                        self.state = 364
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 365
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 366
                        self.match(BKOOLParser.DOT)
                        self.state = 367
                        self.match(BKOOLParser.ID)
                        self.state = 368
                        self.match(BKOOLParser.LB)
                        self.state = 370
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                            self.state = 369
                            self.exprs()


                        self.state = 372
                        self.match(BKOOLParser.RB)
                        pass

             
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exprs(self):
            return self.getTypedRuleContext(BKOOLParser.ExprsContext,0)


        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(BKOOLParser.NEW)
                self.state = 379
                self.match(BKOOLParser.ID)
                self.state = 380
                self.match(BKOOLParser.LB)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 381
                    self.exprs()


                self.state = 384
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def BOOLIT(self):
            return self.getToken(BKOOLParser.BOOLIT, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def sube(self):
            return self.getTypedRuleContext(BKOOLParser.SubeContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def arraylit(self):
            return self.getTypedRuleContext(BKOOLParser.ArraylitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr11)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 391
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.BOOLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 392
                self.match(BKOOLParser.BOOLIT)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 393
                self.match(BKOOLParser.NIL)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 394
                self.sube()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 8)
                self.state = 395
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 9)
                self.state = 396
                self.arraylit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_sube

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSube" ):
                return visitor.visitSube(self)
            else:
                return visitor.visitChildren(self)




    def sube(self):

        localctx = BKOOLParser.SubeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_sube)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(BKOOLParser.LB)
            self.state = 400
            self.expr()
            self.state = 401
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exprs(self):
            return self.getTypedRuleContext(BKOOLParser.ExprsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = BKOOLParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exprs)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.expr()
                self.state = 404
                self.match(BKOOLParser.COMMA)
                self.state = 405
                self.exprs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(BKOOLParser.LSQB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSQB(self):
            return self.getToken(BKOOLParser.RSQB, 0)

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(BKOOLParser.FLOATTYPE, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOATTYPE) | (1 << BKOOLParser.INTTYPE) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 411
            self.match(BKOOLParser.LSQB)
            self.state = 412
            self.match(BKOOLParser.INTLIT)
            self.state = 413
            self.match(BKOOLParser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(BKOOLParser.FLOATTYPE, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def arraytype(self):
            return self.getTypedRuleContext(BKOOLParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPtype" ):
                return visitor.visitPtype(self)
            else:
                return visitor.visitChildren(self)




    def ptype(self):

        localctx = BKOOLParser.PtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_ptype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 415
                self.match(BKOOLParser.INTTYPE)
                pass

            elif la_ == 2:
                self.state = 416
                self.match(BKOOLParser.FLOATTYPE)
                pass

            elif la_ == 3:
                self.state = 417
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 4:
                self.state = 418
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 5:
                self.state = 419
                self.arraytype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ptype(self):
            return self.getTypedRuleContext(BKOOLParser.PtypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_typ)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.ptype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def VOIDTYPE(self):
            return self.getToken(BKOOLParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodtype" ):
                return visitor.visitMethodtype(self)
            else:
                return visitor.visitChildren(self)




    def methodtype(self):

        localctx = BKOOLParser.MethodtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_methodtype)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOATTYPE, BKOOLParser.INTTYPE, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.typ()
                pass
            elif token in [BKOOLParser.VOIDTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(BKOOLParser.VOIDTYPE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def ele_list(self):
            return self.getTypedRuleContext(BKOOLParser.Ele_listContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = BKOOLParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(BKOOLParser.LP)
            self.state = 431
            self.ele_list()
            self.state = 432
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def BOOLIT(self):
            return self.getToken(BKOOLParser.BOOLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle" ):
                return visitor.visitEle(self)
            else:
                return visitor.visitChildren(self)




    def ele(self):

        localctx = BKOOLParser.EleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_ele)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.BOOLIT) | (1 << BKOOLParser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ele(self):
            return self.getTypedRuleContext(BKOOLParser.EleContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def ele_list(self):
            return self.getTypedRuleContext(BKOOLParser.Ele_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ele_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_list" ):
                return visitor.visitEle_list(self)
            else:
                return visitor.visitChildren(self)




    def ele_list(self):

        localctx = BKOOLParser.Ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_ele_list)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.ele()
                self.state = 437
                self.match(BKOOLParser.COMMA)
                self.state = 438
                self.ele_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.ele()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.expr2_sempred
        self._predicates[29] = self.expr3_sempred
        self._predicates[30] = self.expr4_sempred
        self._predicates[31] = self.expr5_sempred
        self._predicates[35] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




