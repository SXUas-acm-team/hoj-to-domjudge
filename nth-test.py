from pycparser.ply.ctokens import t_PLUS

from buildEvent import *
from datetime import datetime
import ndjson
# 更新题目状态信息
# 基本属性，到第几个token，初始化时间、竞赛开始时间、竞赛结束时间

token_cnt = [52]
init_time = datetime(2025, 10, 29, 18, 0, 0)
start_time = datetime(2025, 10, 29, 18, 10, 0)
end_time = datetime(2025, 10, 29, 19, 30, 0)
frozen_time = datetime(2025, 10, 29, 19, 10, 0)
finalize_time = datetime(2025, 10, 29, 19, 40, 0)
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
# 添加比赛开始信息
build_update_info(token_cnt, start_time, None, None, None, init_time, data)
# 添加判题信息
# @parma token编号，提交记录编号，语言id，提交时间，竞赛开始时间，提交队伍id，提交问题id，提交结果(1代表AC,0代表WA)，初始化时间
build_judge_info(token_cnt, 1, "cpp", datetime(2025, 10, 29, 18, 40, 0),start_time, 1, "A", 1, init_time, data)
# 添加比赛封榜信息
build_update_info(token_cnt, start_time, None, frozen_time, None, init_time, data)
# 添加封榜后提交
build_judge_info(token_cnt, 2, "cpp", datetime(2025, 10, 29, 19, 11, 0), start_time, 2, "B", 0, init_time, data)
# 添加比赛结束信息
build_update_info(token_cnt, start_time, end_time, frozen_time, None, init_time, data)
# 添加比赛finalize信息
build_update_info(token_cnt, start_time, end_time, frozen_time, finalize_time, init_time, data)

ndjson.dump(data, open("demo.ndjson", 'w'), ensure_ascii=False)