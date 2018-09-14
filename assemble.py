from datetime import datetime
import ops_briefing.float_extract as float_extract
import ops_briefing.weather_extract as weather_extract

def get_roles(project_name, role_names):
    """
    Returns all assignees for the for a given project and list of roles
    Args:
        roles: List of roles
        project_name: project name
    Returns: Dict of Float tasks
    """
    roles = role_names
    for r in roles:
        roles.update({r["name"]: float_extract.get_assignee(project_name, r)})
    return roles
