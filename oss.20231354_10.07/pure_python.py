f = open("scores.csv", "r",
         encoding = "utf-8")
lines = f.readlines()
f.close()

### 01. 파일 읽기

# print(len(lines))
# print(lines[0])
# print(lines[1])

### 02. 헤더 파싱

#header = lines[0].strip().split(",")
#print(header)

#first = lines[1].strip().split(",")
#print(first)

### 03. 열 위치 찾아 값 꺼내기

header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

#for line in lines[1:4] :
#    parts = line.strip().split(",")
#    print(parts[cat_idx],
#          parts[score_idx])

### 04. 숫자로 바꾸기, 여기서 멈춤

#for line in lines[1:] :
#    parts = line.strip().split(",")
#    score = float(parts[score_idx])
#    print(parts[cat_idx], score)

### 05. 빈 값 건너뛰기, 또 멈춤

#for line in lines[1:] :
#    parts = line.strip().split(",")
#    raw = parts[score_idx].strip()
#    if raw == "":
#        continue
#    score = float(raw)
#    print(parts[cat_idx], score)

### 07. 잘못된 값 건너뛰기

#count = 0
#totals = {}
#counts = {}

#for line in lines[1:] :
#    parts = line.strip().split(",")
#    raw = parts[score_idx].strip()
#    if raw == "":
#        continue
#    try :
#        score = float(raw)
#    except ValueError :
#        continue
#    count = count + 1

#print("사용한 행의 수 : ", count)

### 08. 분류별로 누적하기

count = 0
totals = {}
counts = {}

for line in lines[1:] :
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    try :
        score = float(raw)
    except ValueError :
        continue
    category = parts[cat_idx]
    if category not in totals :
        totals[category] = 0.0
        counts[category] = 0
    totals[category] += score
    counts[category] += 1

    count = count + 1

#print(totals)
#print(counts)


### 09. 평균 계산 및 출력

for c in sorted(totals.keys()) :
    avg = totals[c] / counts[c]
    print(c, round(avg, 2))
