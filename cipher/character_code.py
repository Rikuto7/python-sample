# ASCII
a = 'a'
a10 = ord(a)
a16 = hex(a10)
a2 = bin(a10)

# UTF-8
import sys
# 適用されている文字コード取得
sys.stdin.encoding
a = 'あ'
encode_a = a.encode('utf-8')

# Base64
import os, base64
data = base64.b64encode(os.urandom(32))
