from buildEvent import *
from datetime import datetime
import datetime
import ndjson
import yaml
import csv
# 读取配置文件
with open('contest-info.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
# 首先格式化配置文件中的时间
contest_name = str(data["contest-name"])
contest_init_time_unformatted = str(data["contest-init-time"])
contest_start_time_unformatted = str(data["contest-start-time"])
contest_frozen_time_unformatted = str(data["contest-frozen-time"])
contest_end_time_unformatted = str(data["contest-end-time"])
contest_finalize_time_unformatted = str(data["contest-finalize-time"])

contest_init_time = datetime.datetime.strptime(contest_init_time_unformatted, '%Y-%m-%d %H:%M:%S')
contest_start_time = datetime.datetime.strptime(contest_start_time_unformatted, '%Y-%m-%d %H:%M:%S')
contest_frozen_time = datetime.datetime.strptime(contest_frozen_time_unformatted, '%Y-%m-%d %H:%M:%S')
contest_end_time = datetime.datetime.strptime(contest_end_time_unformatted, '%Y-%m-%d %H:%M:%S')
contest_finalize_time = datetime.datetime.strptime(contest_finalize_time_unformatted, '%Y-%m-%d %H:%M:%S')

# 开始处理event
# 首先载入固定头
data = []
token_cnt = [0]
build_contest_info(token_cnt, contest_name, contest_start_time, contest_end_time, contest_frozen_time, contest_init_time, data)

build_result_info(token_cnt, "AC", contest_init_time, "correct", False, True, data)
build_result_info(token_cnt, "CE", contest_init_time, "compiler error", False, False, data)
build_result_info(token_cnt, "MLE", contest_init_time, "memory limit", True, False, data)
build_result_info(token_cnt, "NO", contest_init_time, "no output", True, False, data)
build_result_info(token_cnt, "OLE", contest_init_time, "output limit", True, False, data)
build_result_info(token_cnt, "RTE", contest_init_time, "run error", True, False, data)
build_result_info(token_cnt, "TLE", contest_init_time, "timelimit", True, False, data)
build_result_info(token_cnt, "WA", contest_init_time, "wrong answer", True, False, data)

build_language_info(token_cnt, "c", "ac6b2c3be82211958c91cde21f27fd26", "gcc --version", "C", ["c"], 1.0, contest_init_time, data)
build_language_info(token_cnt, "cpp", "62531e780378bb346939d18aacdfff1c", "g++ --version", "C++", ["cpp","cc","cxx","c++"], 1.0, contest_init_time, data)
build_language_info_with_runner(token_cnt, "java", "86ba56cb70a79a32c0382214beda8faa", "javac -version","java -version", "Java", ["java"], 1.0,"Main class", contest_init_time, data)
build_language_info_with_runner(token_cnt, "python3", "4e301e4bc46ab73673e209ee3437707d", "pypy3 --version","pypy3 --version", "Python 3", ["py"], 1.0,"Main file", contest_init_time, data)

# 然后处理题目
# 应该先从题目映射表的第一列读取题目
problem_info = []
with open ("n_problem.csv", "r") as problem_csv:
    reader = csv.reader(problem_csv)
    for row in reader:
        problem_info.append(row[0])

for i in range(1, len(problem_info)):
    build_problem_info(token_cnt, problem_info[i], i, 1.0, contest_init_time, data)

# 题目导入完毕后，应该要导入用户组
# 此处先之导入参赛选手组
# TODO: 支持更多用户组的导入

build_group_info(token_cnt, "participants", False, 1, contest_init_time, data)

# 然后导入学校
# 在n_name.csv中获取

school_info_set = set()
with open ("n_name.csv", "r") as name_csv:
    reader = csv.reader(name_csv)
    bypass = -1
    for row in reader:
        bypass += 1
        if bypass == 0:
            continue
        school_info_set.add(row[10])
school_info = dict()
school_info_inverse = dict()
cnt = 0
for i in school_info_set:
    school_info[i] = cnt
    school_info_inverse[cnt] = i
    cnt += 1

for i in range(1, len(school_info_inverse)):
    build_school_info(token_cnt, i, school_info_inverse[i], school_info_inverse[i], "CHN", contest_init_time, data)
ndjson.dump(data, open("converted.ndjson", 'w'), ensure_ascii=False)

# 团队信息
# 只考虑个人参赛，team和user一对一
# team和user信息也应该在n_name中获取
# 需要获取的信息:学校id、学校全程、团队名(用户名)，同时保留团队id以便后文account与团队相对应

#team_info_id 使用牛客id对应用户信息
#学校id school_info获取，学校全程row[10] 团队名row[6]
#team_info_id[i] = {学校全程 团队名, 团队id}

# 需要一个团队对应学校id的表
team_to_school_id = dict()
team_info_id = dict()
cnt = 0
with open ("n_name.csv", "r") as name_csv:
    reader = csv.reader(name_csv)
    bypass = -1
    for row in reader:
        bypass += 1
        if bypass == 0:
            continue
        team_info_id[row[1]] = [row[10], row[6], cnt]
        cnt += 1

for x in team_info_id:
    school_name, name, id = team_info_id[x]
    build_team_info(token_cnt, id, school_info[school_name], False, "participants", school_name, "CHN", name, contest_init_time, data)
    team_to_school_id[id] = school_info[school_name]

# 团队构建完毕(虽然代码写的依托，不过应该不影响)，接下来构建account
# token编号，用户id，队伍id,队伍名，时间，data
for x in team_info_id:
    school_name, name, id = team_info_id[x]
    if(name == "真实名称"):
        continue
    build_user_info(token_cnt, id, id, name, contest_init_time, data)

ndjson.dump(data, open("converted.ndjson", 'w'), ensure_ascii=False)

# 添加比赛开始信息
build_update_info(token_cnt, contest_start_time, None, None, None, contest_init_time, data)
# 终于！开始处理提交信息
# @parma token编号，提交记录编号，语言id，提交时间，竞赛开始时间，提交队伍id，提交问题id，提交结果(1代表AC,0代表WA)，初始化时间, 输出对象
with open ("result.csv", "r") as result_csv:
    reader = csv.reader(result_csv)
    bypass = -1
    for row in reader:
        bypass += 1
        if bypass == 0:
            continue
        uid = row[1]
        problem = row[2]
        school_name = row[3]
        submission_team_id = team_info_id[uid]
        submission_time_unformatted = row[7]
        status = row[6]
        submission_time = datetime.datetime.strptime(submission_time_unformatted, '%Y-%m-%d %H:%M:%S')
        build_judge_info(token_cnt, bypass, "cpp", submission_time, contest_start_time, submission_team_id[2], problem, status, submission_time, data)
# 添加比赛结束信息
build_update_info(token_cnt, contest_start_time, contest_end_time, contest_frozen_time, None, contest_init_time, data)
# 添加比赛finalize信息
build_update_info(token_cnt, contest_start_time, contest_end_time, contest_frozen_time, contest_finalize_time, contest_init_time, data)
ndjson.dump(data, open("converted.ndjson", 'w'), ensure_ascii=False)