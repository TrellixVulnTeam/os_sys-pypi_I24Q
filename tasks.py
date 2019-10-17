from invoke import task, run

@task
def build(ctx, clean=False):
    if clean:
        print("Cleaning!")
    print("Building!")
def cmds(commands):
    def run(commands):
        import sys
        from subprocess import Popen, PIPE, STD_INPUT_HANDLE
        mystring = ''
        process = Popen( "cmd.exe", shell=False, universal_newlines=True, stdin=STD_INPUT_HANDLE, stdout=PIPE, stderr=PIPE)
        for st in commands:
            mystring = mystring + st + '\n'
        out, err = process.communicate(mystring)
        return [out, err]
    return run(commands)
@task(help={"remove": "remove dirs: build, dist and os_sys.egg-info"})
def remove(ctx):
    import shutil
    """remove dirs:
build
dist
os_sys.egg-info
    after using it"""
    try:
        shutil.rmtree(r'C:\mattie\own lib\own lib\dist')
        shutil.rmtree(r'C:\mattie\own lib\own lib\os_sys.egg-info')
        shutil.rmtree(r'C:\mattie\own lib\own lib\build')
    except Exception as ex:
        print(ex)
        print(ex.__class__)
        raise ex
@task
def update(ctx):
    import shutil
    """remove dirs:
    build
    dist
    os_sys.egg-info
    after using it
    """
    ctx.run('update_lib')
    try:
        shutil.rmtree(r'C:\mattie\own lib\own lib\dist')
        shutil.rmtree(r'C:\mattie\own lib\own lib\os_sys.egg-info')
        shutil.rmtree(r'C:\mattie\own lib\own lib\build')
    except:
        pass
