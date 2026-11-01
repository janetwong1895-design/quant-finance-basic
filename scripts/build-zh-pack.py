# coding: utf-8
"""Build the translated learner pack without solutions or external dependencies."""
from pathlib import Path
import json, zipfile
root=Path(__file__).resolve().parents[1]
out=root/'dist/zh-tw/python'
spec=json.loads((out/'exercises.json').read_text(encoding='utf-8'))
check='''# -*- coding: utf-8 -*-
"""執行：python3 check.py ch1-allocation；或 python3 check.py all。"""
import argparse
import json
import runpy
from pathlib import Path
from checker import run_checks
here = Path(__file__).resolve().parent
spec = json.loads((here / "exercises.json").read_text(encoding="utf-8"))
parser = argparse.ArgumentParser(description="檢查儲存的學習程式；不會上傳程式碼。")
parser.add_argument("exercise", choices=[item["id"] for item in spec] + ["all"])
args = parser.parse_args()
selected = spec if args.exercise == "all" else [item for item in spec if item["id"] == args.exercise]
failed = False
for exercise in selected:
    try:
        namespace = runpy.run_path(str(here / (exercise["id"] + ".py")), run_name="__practice__")
        results = json.loads(run_checks(namespace, json.dumps(exercise["cases"])))
        print("\\n" + exercise["id"] + " " + exercise["title"])
        for result in results:
            print(("通過" if result["passed"] else "重新檢查"), result["label"], "-", result["message"])
        passed = sum(result["passed"] for result in results)
        print(str(passed) + "/" + str(len(results)) + " 項數值檢查通過。請另外解釋結果與限制。")
        failed = failed or passed != len(results)
    except (SyntaxError, NameError, TypeError, ValueError) as exc:
        print(type(exc).__name__ + ": " + str(exc))
        print("檢查縮排、名稱與尚未替換的 None，再修改重試。")
        failed = True
raise SystemExit(1 if failed else 0)
'''
checker=(root/'dist/python/checker.py').read_text(encoding='utf-8')
for a,b in {'Expected behaviour matched.':'預期行為相符。','Expected a finite numeric result.':'預期為有限的數值結果。','Check the function name and arguments.':'請檢查函式名稱與參數。','Define the function ':'請定義函式 ',' with the supplied arguments.':'，並使用提供的參數。','Result or units differ. ':'結果或單位不符。',' Keep full precision inside functions.':' 函式內請保留完整精度。','Replace the TODO line, then run and check again. ':'請替換 TODO 行，再執行與檢查。'}.items():checker=checker.replace(a,b)
(out/'checker.py').write_text(checker,encoding='utf-8')
(out/'check.py').write_text(check,encoding='utf-8')
readme='''量化金融基礎｜臺灣繁體中文 Python 學習包

金額採新臺幣（TWD／NT$），為假設教學情境，並非匯率換算。
數字顯示例如 NT$1,234.56；程式計算使用未加千位逗號的數值。
需要 Python 3.8 以上，僅使用標準函式庫，不需 pip 安裝。
在此資料夾執行 python3 check.py ch1-change；Windows 可用 py。
把活動代碼換成其他檔名（不含 .py）即可檢查，all 表示全部。
成功結束碼 0、尚有未通過 1、錯誤參數 2。
請先預測、完成 TODO、檢查、解釋，再保留具體修正與限制。
exercises.json 含完整中文目標、說明、提示與測試規格；各 .py 保留英文語法、識別字及程式內註解。原生錯誤訊息也可能為英文。
此包不含參考解答；完整中文文字指南位於網站 python/guide.html。
本機紀錄不會同步瀏覽器。不得輸入密碼或個人財務資料；不需金融帳戶。
這是形成性自學，不提供獨立評分、能力認證或投資建議。
'''
with zipfile.ZipFile(out/'learner-pack.zip','w',zipfile.ZIP_DEFLATED) as z:
    for name,text in [('README.txt',readme),('check.py',check),('checker.py',checker),('exercises.json',json.dumps(spec,ensure_ascii=False,indent=2))]:
        info=zipfile.ZipInfo(name,(2026,11,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,text.encode('utf-8'))
    for e in spec:
        info=zipfile.ZipInfo(e['id']+'.py',(2026,11,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,e['starter'].encode('utf-8'))
print('Built reproducible Taiwan Chinese learner pack: 26 starters, Chinese instructions/checks, no solutions.')
