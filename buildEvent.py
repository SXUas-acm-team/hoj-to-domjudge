import csv
import ndjson
from datetime import datetime
data = []
# 构建竞赛信息
def build_contest_info(token_id, contest_name, start_time, end_time, time, data):
    iso_start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    iso_end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token":str(token_id[0]),
        "id":None,
        "type":"contest",
        "data":
            {
                "formal_name": "三晋七校ACM队招新联赛",
                "scoreboard_type": "pass-fail",
                "start_time": iso_start_time,
                "end_time": iso_end_time,
                "scoreboard_thaw_time": None,
                "duration": "5:00:00.000",
                "scoreboard_freeze_duration": "1:00:00.000",
                "cid": 1,
                "id": "external-id-submit-demo",
                "name": "首届三晋七校ACM队招新联赛",
                "shortname": "三晋七校ACM队招新联赛",
                "allow_submit": True,
                "runtime_as_score_tiebreaker": None,
                "warning_message": None,
                "penalty_time": 20
            },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x
# 构建提交后的判题信息
# @Parma:token编号，判题状态("AC","WA")，构造时间，全程("correct", "wrong answer"), 是否叠罚时，是否算通过
def build_result_info(token_id, id, time, name, penalty, solved, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token": str(token_id[0]),
        "id": id,
        "type": "judgement-types",
        "data":{
            "id": id,
            "name": name,
            "penalty":penalty,
            "solved":solved
        },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x
# 构建允许的语言信息
# @parma token编号，语言id，语言哈希，编译指令，语言名，支持的语言后缀，时间倍数，构造时间
def build_language_info(token_id, id, hash, command, name, extension, time_factor, time, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token": str(token_id[0]),
        "id": id,
        "type": "languages",
        "data":{
            "compile_executable_hash":hash,
            "compiler":{
                "version_command":command
            },
            "id": id,
            "name": name,
            "extensions":extension,
            "filter_compiler_files": True,
            "allow_judge": True,
            "time_factor": time_factor,
            "entry_point_required": False,
            "entry_point_name": None
        },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x
def build_language_info_with_runner(token_id, id, hash, command, runner, name, extension, time_factor, entry_point, time, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token": str(token_id[0]),
        "id": id,
        "type": "languages",
        "data":{
            "compile_executable_hash":hash,
            "compiler":{
                "version_command":command
            },
            "runner":{
                "version_command":runner
            },
            "id": id,
            "name": name,
            "extensions":extension,
            "filter_compiler_files": True,
            "allow_judge": True,
            "time_factor": time_factor,
            "entry_point_required": False,
            "entry_point_name": "Main class"
        },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x

# 构建初始化题目信息
# @Parma:token编号，题目题号(通常为大写单字母)，题目编号，题目时限，构建时间
def build_problem_info(token_id, id, problem_cnt, time_limit, time, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token": str(token_id[0]),
        "id": id,
        "type": "problems",
        "data":{
            "ordinal": problem_cnt,
            "probid": problem_cnt,
            "shortname": id,
            "rgb": None,
            "color": None,
            "label": id,
            "time_limit": time_limit,
            "statement":[],
            "attachments":[],
            "id": id,
            "name": id,
            "test_data_count": 1
        },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x

# 构建用户组信息
# @parma token编号，用户组名， 是否在滚榜时隐藏，用户组编号， 构建时间
def build_group_info(token_id, id, hidden, categoryid, time, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token": str(token_id[0]),
        "id": id,
        "type": "groups",
        "data":{
            "hidden":hidden,
            "categoryid": categoryid,
            "id": id,
            "icpc_id": None,
            "name": id,
            "sortorder": 0,
            "color": None,
            "allow_self_registration": False
        },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x

# 构建学校信息
# @parma token编号，学校编号，学校全程，学校简称，学校所属国家，构建时间
def build_school_info(token_id, id, name, short_name, country, time, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token": str(token_id[0]),
        "id": str(id),
        "type": "organizations",
        "data":{
            "shortname": short_name,
            "affilid": id,
            "id": str(id),
            "icpc_id": str(id),
            "name": short_name,
            "formal_name": name,
            "country": country,
            "country_flag":
                [

                    {
                        "href": "country-flags/" + country +"/4x3",
                        "mime": "image/svg+xml",
                        "filename": "country-flag-4x3.svg",
                        "width": 640,
                        "height": 480
                    },
                    {
                        "href": "country-flags/"+country+"/1x1",
                        "mime": "image/svg+xml",
                        "filename": "country-flag-1x1.svg",
                        "width": 512,
                        "height": 512
                    }
                ]
        },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x
# 添加团队信息
# @parma: token编号，队伍编号，所属学校id，是否隐藏，所属用户组id，学校全程，学校名，国家，团队名，初始化时间
def build_team_info(token_id, id, organization_id, hidden, group_id, school, country, team_name, time, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token": str(token_id[0]),
        "id": str(id),
        "type": "teams",
        "data": {
            "location": None,
            "organization_id": str(organization_id),
            "hidden": hidden,
            "group_ids":
            [
                group_id
            ],
            "affiliation": school,
            "nationality": country,
            "teamid": str(id),
            "id": str(id),
            "icpc_id": str(id),
            "label": str(id),
            "name": team_name,
            "display_name": None,
            "public_description": None
        },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x
# 添加用户信息
# token编号，用户id，用户名，队伍id，队伍名，初始化时间
# 用户信息id用于登录系统，用户属于队伍，实际显示为队伍名
def build_user_info(token_id, user_id, team_id, team_name, time, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    x = {
        "token": str(token_id[0]),
        "id": str(user_id),
        "type": "accounts",
        "data":{
            "last_login_time": None,
            "last_api_login_time": None,
            "first_login_time": None,
            "team": team_name,
            "team_id": str(team_id),
            "roles":["team"],
            "type": "team",
            "userid": int(user_id),
            "id": str(user_id),
            "username": str(user_id),
            "name": str(user_id),
            "email": None,
            "last_ip": None,
            "ip": None,
            "enabled": True
        },
        "time": iso_time
    }
    token_id[0] += 1
    data.append(x)
    return x
# 添加提交判题信息
# @parma token编号，提交记录编号，语言id，提交时间，竞赛开始时间，提交队伍id，提交问题id，提交结果(1代表AC,0代表WA)，初始化时间
def build_judge_info(token_id, submission_id, language_id, submission_time, start_time, team_id, problem_id, result, time, data):
    iso_time = time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    sub_time = submission_time.strftime("%Y-%m-%dT%H:%M:%S.000+08:00")
    contest_time = submission_time - start_time
    con_time = "{:02d}:{:02d}:{:02d}.000".format(contest_time.days, contest_time.seconds // 3600, (contest_time.seconds % 3600) // 60,contest_time.seconds % 60)
    #con_time = contest_time.strftime("%H:%M:%S.000")
    judgement_result = "AC"
    if result == 0:
        judgement_result = "WA"
    a1 = {
        "token": str(token_id[0]),
        "id": str(submission_id),
        "type": "submissions",
        "data":{
            "language_id": language_id,
            "time":str(sub_time),
            "contest_time":con_time,
            "team_id": str(team_id),
            "problem_id": problem_id,
            "files":[
                {
                    "href": "contests/external-id-submit-demo/submissions/" + str(submission_id) +"/files",
                    "mime": "application/zip", "filename": "submission.zip"
                }
            ],
            "submitid": int(submission_id),
            "id": str(submission_id),
            "entry_point": None,
            "import_error": None
        },
        "time": sub_time
    }
    token_id[0] += 1
    a2 = {
        "token": str(token_id[0]),
        "id": str(submission_id),
        "type": "judgements",
        "data":{
            "start_time": sub_time,
            "start_contest_time": con_time,
            "end_time": None,
            "end_contest_time": None,
            "max_run_time": None,
            "submission_id": str(submission_id),
            "id": str(submission_id),
            "valid": True,
            "judgement_type_id": None
        },
        "time": sub_time
    }
    token_id[0] += 1
    a3 = {
        "token": str(token_id[0]),
        "id": str(submission_id),
        "type": "runs",
        "data":{
            "run_time":0.001,
            "time": sub_time,
            "contest_time": con_time,
            "judgement_id": str(submission_id),
            "ordinal": 1,
            "id": submission_id,
            "judgement_type_id": judgement_result
        },
        "time": sub_time
    }
    token_cnt[0] += 1
    a4 = {
        "token": str(token_cnt[0]),
        "id": str(submission_id),
        "type": "judgements",
        "data":{
            "start_time": sub_time,
            "start_contest_time": con_time,
            "end_time": sub_time,
            "end_contest_time": con_time,
            "max_run_time": 0.001,
            "submission_id": str(submission_id),
            "id": str(submission_id),
            "valid": True,
            "judgement_type_id": judgement_result
        },
        "time": sub_time
    }
    token_cnt[0] += 1
    data.append(a1)
    data.append(a2)
    data.append(a3)
    data.append(a4)
    return ""
# 构建竞赛状态更新信息:
def build_update_info(token_cnt, id, start, end, forzen, finalized, time, data):
    pass

# 更新题目状态信息
# 基本属性，到第几个token，初始化时间、竞赛开始时间、竞赛结束时间
token_cnt = [52]
init_time = datetime(2025, 10, 29, 18, 0, 0)
start_time = datetime(2025, 10, 29, 18, 10, 0)
end_time = datetime(2025, 10, 29, 19, 30, 0)
# 首先构建竞赛基本信息
build_contest_info(token_cnt, "首届三晋七校ACM队招新联赛", start_time, end_time, init_time, data)

# 添加judge结果信息
build_result_info(token_cnt, "AC", init_time, "correct", False, True, data)
build_result_info(token_cnt, "CE", init_time, "compiler error", False, False, data)
build_result_info(token_cnt, "MLE", init_time, "memory limit", True, False, data)
build_result_info(token_cnt, "NO", init_time, "no output", True, False, data)
build_result_info(token_cnt, "OLE", init_time, "output limit", True, False, data)
build_result_info(token_cnt, "RTE", init_time, "run error", True, False, data)
build_result_info(token_cnt, "TLE", init_time, "timelimit", True, False, data)
build_result_info(token_cnt, "WA", init_time, "wrong answer", True, False, data)
#添加支持的语言
# @parma token编号，语言id，语言哈希，编译指令，语言名，支持的语言后缀，时间倍数，构造时间
build_language_info(token_cnt, "c", "ac6b2c3be82211958c91cde21f27fd26", "gcc --version", "C", ["c"], 1.0, init_time, data)
build_language_info(token_cnt, "cpp", "62531e780378bb346939d18aacdfff1c", "g++ --version", "C++", ["cpp","cc","cxx","c++"], 1.0, init_time, data)
build_language_info_with_runner(token_cnt, "java", "86ba56cb70a79a32c0382214beda8faa", "javac -version","java -version", "Java", ["java"], 1.0,"Main class", init_time, data)
build_language_info_with_runner(token_cnt, "python3", "4e301e4bc46ab73673e209ee3437707d", "pypy3 --version","pypy3 --version", "Python 3", ["py"], 1.0,"Main file", init_time, data)
# 添加题目
build_problem_info(token_cnt, "A", 1, 1.0, init_time, data)
build_problem_info(token_cnt, "B", 2, 1.0, init_time, data)
build_problem_info(token_cnt, "C", 3, 1.0, init_time, data)
build_problem_info(token_cnt, "D", 4, 1.0, init_time, data)
build_problem_info(token_cnt, "E", 5, 1.0, init_time, data)
build_problem_info(token_cnt, "F", 6, 1.0, init_time, data)
build_problem_info(token_cnt, "G", 7, 1.0, init_time, data)
build_problem_info(token_cnt, "H", 8, 1.0, init_time, data)
build_problem_info(token_cnt, "I", 9, 1.0, init_time, data)
# 添加参赛选手用户组
build_group_info(token_cnt, "participants", False, 1, init_time, data)
#添加学校信息
build_school_info(token_cnt, 1, "Shanxi University", "SXU","CHN",init_time, data)
build_school_info(token_cnt, 2, "North University of China", "NUC","CHN",init_time, data)
# 添加团队信息
build_team_info(token_cnt, 1, 1, False, "participants", "Shanxi University", "CHN", "SXU-01", init_time, data)
build_team_info(token_cnt, 2, 1, False, "participants", "Shanxi University", "CHN", "SXU-02", init_time, data)
build_team_info(token_cnt, 3, 2, False, "participants", "North University of China", "CHN", "NUC-01", init_time, data)
build_team_info(token_cnt, 4, 2, False, "participants", "North University of China", "CHN", "NUC-02", init_time, data)
# 添加用户信息
build_user_info(token_cnt,1, 1, "SXU-01",init_time, data)
build_user_info(token_cnt,2, 2, "SXU-02",init_time, data)
build_user_info(token_cnt,3, 3, "NUC-01",init_time, data)
build_user_info(token_cnt,4, 4, "NUC-02",init_time, data)
# 添加判题信息
# @parma token编号，提交记录编号，语言id，提交时间，竞赛开始时间，提交队伍id，提交问题id，提交结果(1代表AC,0代表WA)，初始化时间
build_judge_info(token_cnt, 1, "cpp", datetime(2025, 10, 29, 18, 40, 0),start_time, 1, "A", 1, init_time, data)
# 添加竞赛结束信息

ndjson.dump(data, open("demo.ndjson", 'w'), ensure_ascii=False)