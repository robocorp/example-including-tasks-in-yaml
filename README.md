# Including Robot Tasks in robot.yaml

This robot demonstrates how to add all your Robot tasks defined in the `tasks.robot` file
into `robot.yaml`.

This is basically achieved by (1) adding additional `tasker.yaml` and `tasker.py` files into your existing Robot directory and (2) by adding PyPI dependency `PyYAML==5.4.1` into `conda.yaml`.

When that is done just run:

```shell
rcc run -r tasker.yaml
```

Command will parse `tasks.robot` file and creates a new `modified_robot.yaml` file into the same directory.

Modify `tasker.py` variable `result_robot_yaml` to `result_robot_yaml = original_robot_yaml` if you want to replace `robot.yaml` content.
