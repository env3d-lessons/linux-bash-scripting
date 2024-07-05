import pathlib
import os
import re
import urllib.request

def file_basic_check(f):
    # Test file existence and not empty
    assert pathlib.Path(f).is_file()
    assert pathlib.Path(f).stat().st_size > 0

def file_regex(f, regex):
    # Test the content of a file against a regex
    with open(f) as fi:
        text = fi.read()
        return re.search(regex, text)
    
def test_download_sh():
    file_basic_check('download.sh')

def test_download_sh_hashbang():
    assert file_regex('download.sh', '^#!')

def test_download_sh_content():
    assert file_regex('download.sh', r'curl.+langara\.ca.+|.+grep')

def test_download_sh_exec():
    os.popen('./download.sh').read()
    p = pathlib.Path('.')
    jpg_files = list(p.glob('./*.jpg'))
    assert len(jpg_files) > 0, "jpg files not downloaded"
    os.popen('rm ./*.jpg').read()
    
def test_q2a():
    file_basic_check('q2a.txt')

def test_q2a_exec():
    result = os.popen('bash q2a.txt').read()
    l = result.split('\n')
    assert len([ i for i in l if len(i) > 0 ] ) == 150, "incorrect number of directories returned"
    assert len([ i for i in l if 'dog' in i ]) == 150, "incorrect directory names"
    assert len([ i for i in l if i.endswith('/')]) == 150, "incorrect directory names"

def test_dog_image():
    file_basic_check('dog_image.sh')

def test_dog_image_exec():
    result = os.popen('./dog_image.sh').readlines()
    assert len(result) < 10
    for url in result:
        r = urllib.request.urlopen(url)
        assert r.getcode() == 200



