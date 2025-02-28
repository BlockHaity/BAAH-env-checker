import json
import subprocess
import sys
import os
import urllib.request

def help():
        print('BAAH env checker')
        print('BAAH环境检查器')
        print('')
        print('用法: python3 checker.py <功能> <选项>')
        print('功能:')
        print('  fix - 尝试修复环境')
        print('  check - 检查环境并生成报告')
        print('  help - 显示帮助信息')
        print('  version - 显示版本信息')
        print('选项:')
        print('  当使用 check 功能时:')
        print('    system - 检查系统环境')
        print('    python - 检查Python环境')
        print('    docker - 检查docker环境')
        print('  当使用 fix 功能时:')
        print('    env - 修复python venv环境')
        print('    requirements - 修复requirements.txt')

def version():
    print('BAAH env checker 1.0.0')
    print('BAAH环境检查器 1.0.0')

if __name__ == '__main__':
    if len(sys.argv) >= 1:
        if sys.argv[1] == 'version':
            version()
        elif sys.argv[1] == 'help':
            help()
        elif sys.argv[1] == 'check':
            if len(sys.argv) >= 3:
                if sys.argv[2] == 'system':
                    version()
                    # 检查系统环境
                    if sys.platform == 'win32':
                        print('系统: Windows')
                        if sys.getwindowsversion().major < 10:
                            print(f'Windows版本: {sys.getwindowsversion().major}')
                            report = {'platform': 'Windows'}
                            report['version'] = sys.getwindowsversion().major
                            report['error'] = 'system-not-support'
                            with open('report-system.json', 'w', encoding='utf-8') as f:
                                json.dump(report, f)
                            print('报告已生成: report-system.json')
                            print('[error][system-not-support]请升级您的Windows版本到10或更高版本。')
                        elif sys.getwindowsversion().major == 10:
                            print(f'Windows版本: {sys.getwindowsversion().major}')
                            report = {'platform': 'Windows'}
                            report['version'] = sys.getwindowsversion().major
                            with open('report-system.json', 'w', encoding='utf-8') as f:
                                json.dump(report, f)
                            print('报告已生成: report-system.json')
                            print('[info]您的Windows版本为10，可以继续使用。')
                        if sys.getwindowsversion().major == 11:
                            print(f'Windows版本: {sys.getwindowsversion().major}')
                            report = {'platform': 'Windows'}
                            report['version'] = sys.getwindowsversion().major
                            with open('report-system.json', 'w', encoding='utf-8') as f:
                                json.dump(report, f)
                            print('报告已生成: report-system.json')
                            print('[info]您的Windows版本为11，可以继续使用。')
                    elif sys.platform == 'linux':
                        print('系统: Linux')
                        report = {'platform': 'Linux'}
                        linux_id = subprocess.run(['lsb_release', '-is'], capture_output=True, text=True).stdout.strip()
                        linux_id_data = requests.get(f'https:/').text
                            
                elif sys.argv[2] == 'python':

                elif sys.argv[2] == 'docker':
    else:
        help()