import requests
import os
from kommons import KairosException
from datetime import datetime

FLOAT_API = "https://api.float.com/v3/"
FLOAT_HEADER = {"Authorization": "Bearer {}".format(os.environ["FLOAT_KEY"])}


def get_project_id(project_name):
    """
    Returns project ID for a given project name
    Args:
        project_name: project name
    Returns: Float Project ID
    """
    projects = requests.get(FLOAT_API + "projects?per_page=200", headers=FLOAT_HEADER).json()
    pid = [p["project_id"] for p in projects if p["name"] in project_name]
    if len(pid) == 0:
        raise KairosException("Project {} not found in Float".format(project_name))
    elif len(pid) > 1:
        raise KairosException("Multiple projects match name {}: {}".format(project_name, pid))
    else:
        return pid[0]

def get_task_id(pid, task_name):
    """
    Returns task ID for a given task name
    Args:
        task_name: task name
    Returns: Float Task ID
    """
    datestr = date.strftime("%Y-%m-%d")
    tasks = requests.get(FLOAT_API + "tasks?project_id={}&start_date={}&end_date={}&per_page=200".format(pid,
                                                                                                        datestr,
                                                                                                        datestr),
                                                                                    headers=FLOAT_HEADER).json()
    tid = [t["task_id"] for r in roles if r["name"] in role_name]
    if len(tid) == 0:
        raise KairosException("Role {} not found in Float".format(task_name))
    elif len(tid) > 1:
        raise KairosException("Multiple roles match name {}: {}".format(task_name, tid))
    else:
        return tid[0]

def get_people_id(tid):
    """
    Returns people ID for a given task ID
    Args:
        tid: Float Task ID
    Returns: Float People ID
    """
    people = requests.get(FLOAT_API + "tasks?per_page=200", headers=FLOAT_HEADER).json()
    nid = [n["people_id"] for n in roles if n["task_id"] in tid]
    if len(nid) == 0:
        raise KairosException("Nobody is assigned to task_ID {}".format(tid))
    elif len(nid) > 1:
        raise KairosException("Multiple people match task_ID {}: {}".format(tid, nid))
    else:
        return nid[0]

def get_name(nid):
    """
    Returns names for a given people ID
    Args:
        nid: Float People ID
    Returns: Name
    """
    names = requests.get(FLOAT_API + "people?per_page=200.format(rid)", headers=FLOAT_HEADER).json()
    name = [n["name"] for n in names if n["people_id"] in nid]
    if len(name) == 0:
        raise KairosException("Person ID {} not found in Float".format(nid))
    elif len(name) > 1:
        raise KairosException("Multiple names match person ID {}: {}".format(nid, name))
    else:
        return name[0]

def get_assignee(project_name, task_name):
    pid = get_project_id(project_name)
    tid = get_task_id(pid, task_name)
    nid = get_people_id(tid)
    assignee = get_name(nid)
    return assignee

    def main(project_name, task_name):
        assignee = get_assignee (project_name, task_name)
        print(assignee)

    if __name__ == "__main__":
        main("Permian Basin (PNR) - Methane 1-1", "Data Analyst")
