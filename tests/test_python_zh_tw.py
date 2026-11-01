"""Verify the translated offline pack and checker contracts without a network."""
import json
import runpy
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist/zh-tw/python'

class TaiwanPackTests(unittest.TestCase):
    def test_all_translated_reference_cases_pass(self):
        spec=json.loads((OUT/'exercises.json').read_text(encoding='utf-8'))
        check=runpy.run_path(str(OUT/'checker.py'))['run_checks']
        for e in spec:
            namespace=runpy.run_path(str(OUT/'reference'/(e['id']+'.py')),run_name='__practice__')
            result=json.loads(check(namespace,json.dumps(e['cases'])))
            self.assertTrue(all(r['passed'] for r in result),e['id'])
            self.assertTrue(all('預期行為相符' in r['message'] for r in result))

    def test_translated_pack_is_self_contained_and_all_command_runs_every_activity(self):
        spec=json.loads((OUT/'exercises.json').read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp,zipfile.ZipFile(OUT/'learner-pack.zip') as z:
            self.assertNotIn('reference/', ' '.join(z.namelist()))
            self.assertIn('繁體中文',z.read('README.txt').decode('utf-8'))
            z.extractall(tmp)
            for e in spec:self.assertEqual((Path(tmp)/(e['id']+'.py')).read_text(),e['starter'])
            one=subprocess.run([sys.executable,'check.py','ch1-change'],cwd=tmp,capture_output=True,text=True)
            self.assertEqual(one.returncode,0,one.stderr)
            self.assertIn('通過',one.stdout)
            all_result=subprocess.run([sys.executable,'check.py','all'],cwd=tmp,capture_output=True,text=True)
            self.assertEqual(all_result.returncode,1,all_result.stderr)
            for e in spec:self.assertIn(e['id'],all_result.stdout)
            invalid=subprocess.run([sys.executable,'check.py','nonexistent'],cwd=tmp,capture_output=True,text=True)
            self.assertEqual(invalid.returncode,2)

if __name__=='__main__':unittest.main()
