﻿import sys
input = lambda: sys.stdin.readline().strip()

print('\n'.join(map(str, sorted([int(input()) for _ in range(int(input()))]))))