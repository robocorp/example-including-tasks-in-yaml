from robot.api.parsing import get_tokens
import yaml

robot_filename = "tasks.robot"
original_robot_yaml = "robot.yaml"
result_robot_yaml = (
    "modified_robot.yaml"  # set to original_robot_yaml if you want to modify original
)


class MyDumper(yaml.SafeDumper):
    linebreaked = False  # Used to insert linebreak only once
    # HACK: insert blank lines between top-level objects
    # inspired by https://stackoverflow.com/a/44284819/3786245
    def write_line_break(self, data=None):
        super().write_line_break(data)

        if len(self.indents) == 1 and not self.linebreaked:
            super().write_line_break()
            self.linebreaked = True


def get_all_tasks():
    tasks = []
    for token in get_tokens(robot_filename):
        if token.type == "TESTCASE NAME":
            tasks.append(str(token.value))
    return tasks


if __name__ == "__main__":
    tasks = get_all_tasks()
    if len(tasks) == 0:
        raise ValueError("The '%s' does not contain any tasks" % robot_filename)

    data = None
    with open(original_robot_yaml, "r") as yaml_in:
        data = yaml.safe_load(yaml_in)

    data["tasks"] = {}
    for t in tasks:
        data["tasks"][t] = {"robotTaskName": t}

    with open(result_robot_yaml, "w") as yaml_out:
        yaml.dump(data, yaml_out, Dumper=MyDumper, sort_keys=False)
