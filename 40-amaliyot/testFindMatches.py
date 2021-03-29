import unittest
from uzwords import words
from findMatches import findMatches

class wordTest(unittest.TestCase):
    def test_matches(self):
        test1 = {'word':'олти','matches': ['ит', 'лит', 'лот', 'о', 'ол', 'от', 'отли', 'тил', 'то', 'тол']}
        test2 = {'word':'аллома','matches': ['а', 'алам', 'алла', 'алло', 'ало', 'амал', 'лама', 'лол', 'лола', 'лом', 'ма', 'малла', 'малол', 'мол', 'мола', 'о', 'ол', 'ола', 'олам', 'олма', 'ом']}
        test3 = {'word':'тараққиёт','matches': ['а', 'аё', 'аёқ', 'ар', 'арақ', 'арақи', 'ари', 'ариқ', 'атир', 'атиқа', 'ақиқ', 'ақиқа', 'ирқ', 'ит', 'итёқа', 'иқ', 'риё', 'риққат', 'тар', 'тарақ', 'тариқ', 'тариқа', 'тариқат', 'татар', 'татир', 'татиқ', 'таёқ', 'тақ', 'тақа', 'тақир', 'тақиқ', 'таққа', 'тир', 'тиқ', 'ё', 'ёр', 'ёри', 'ёриқ', 'ёрти', 'ёт', 'ётиқ', 'ёқ', 'ёқа', 'ёқиқ', 'ёқти', 'қаратқи', 'қари', 'қарт', 'қарта', 'қат', 'қатиқ', 'қатра', 'қаттиқ', 'қақир', 'қир', 'қирт', 'қирқ', 'қиё', 'қиёт', 'қиёқ']}
        self.assertEqual(set(test1['matches']),set(findMatches(test1['word'],words)))
        self.assertEqual(set(test2['matches']),set(findMatches(test2['word'],words)))
        self.assertEqual(set(test3['matches']),set(findMatches(test3['word'],words)))

unittest.main()