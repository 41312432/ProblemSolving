# 7. String (문자열)

> https://www.acmicpc.net/step/7

1. 11654 아스키 코드
   ```py
   ord(character) # return ASCCII number
   chr(ASCII number) #return Character
   ```
2. 11720 숫자의 합
3. 10809 알파벳 찾기
   ```py
   [a...z] == list(map(chr, range(97, 123)))
   ```
4. 2675 문자열 반복
5. 1157 단어 공부
6. 1152 단어의 개수
   ```py
   import collections.Counter
   ```
7. 2908 상수
8. 5622 다이얼
9. 2941 크로아티아 알파벳

   ```py
   #Short Coding Ver
   sep = ['=', '-', 'dz=', 'lj', 'nj']
   s = input()
   print(len(s) - sum(s.count(c)) for c in sep)
   ```

10. 1316 그룹 단어 체커
