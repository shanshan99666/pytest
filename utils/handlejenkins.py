# handlejenkins
# 2022/10/14
# coding: utf-8
import jenkins


# create jenkins server,return the result
def create_jenkins_server(url, username, password):
    server = jenkins.Jenkins(url, username, password)
    return server


# create job, return job name
def create_job(server, job_name, job_config):
    server.create_job(job_name, job_config)
    return job_name


# build job, return build result
def build_job(server, job_name):
    result = server.build_job(job_name)
    return result


# copy job, return job name
def copy_job(server, job_name, new_job_name):
    server.copy_job(job_name, new_job_name)
    return new_job_name


# delete job, return result of delete
def delete_job(server, job_name):
    result = server.delete_job(job_name)
    return result


# get job config, return job config
def get_job_config(server, job_name):
    job_config = server.get_job_config(job_name)
    return job_config


# get job info, return job info
def get_job_info(server, job_name):
    job_info = server.get_job_info(job_name)
    return job_info


# active job, !!!! first step disable job,second step enable job !!!!,return result of active
def active_job(server, job_name):
    result = server.disable_job(job_name)
    result = server.enable_job(job_name)
    return result


if __name__ == '__main__':
    # create jenkins server
    url = 'http://xx.xx.xx.xx:8080/jenkins'
    user = 'xxxx'
    passwd = 'xxxx'
    server = create_jenkins_server(url, user, passwd)

    # create job
    job_name = 'test_job'
    job_config = '''<project>
    <actions/>
    <description></description>
    
    </project>'''
    create_job(server, job_name, job_config)
    print('create job success')

    # copy job
    new_job_name = 'test_job_copy5'
    copy_job(server, job_name, new_job_name)
    print(new_job_name)

    # active job
    active_job(server, new_job_name)
    print('active job success')

    # build job
    build_result = build_job(server, new_job_name)
    print(build_result)

    # delete job
    delete_job(server, job_name)
    print('delete job success')

    # get job config
    job_config = get_job_config(server, new_job_name)
    print(job_config)

    # get job info
    job_info = get_job_info(server, new_job_name)
    print(job_info)