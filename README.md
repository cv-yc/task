
# Task

机器人社考核任务项目。包含一个计算器模块，以及配套的脚本和测试。

## 环境要求

- Python 3.12（由 `.python-version` 指定）
- uv（依赖管理工具）

### 安装 uv

如果还没装 uv，执行：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

装完后重开终端，用 `uv --version` 确认。

## 安装依赖

```bash
cd ~/Robotics/task
uv sync
```

或使用脚本：

```bash
bash scripts/setup_env.sh
```

## 运行游戏示例

```bash
uv run python example/GuessingGame.py
```

或使用脚本：

```bash
bash scripts/run_game.sh
```

游戏玩法：程序会随机生成一个数字，你输入猜测的数字，程序提示"大了"或"小了"，猜中即胜。

## 运行测试

```bash
uv run pytest tests/
```

或运行单个测试文件：

```bash
uv run pytest tests/test_calculate.py
```

或使用脚本：

```bash
bash scripts/check.sh
```


## 目录结构

```text
task/
├── example/
│   └── GuessingGame.py   # 猜数字游戏示例
├── scripts/
│   ├── setup_env.sh      # 安装依赖（uv sync）
│   ├── check.sh          # 运行测试（pytest）
│   └── run_game.sh       # 运行猜数字游戏
├── src/
│   └── task/
│       ├── __init__.py
│       └── calculate.py  # 计算器模块（加、减、乘、除、取整、取余、幂）
├── tests/
│   └── test_calculate.py # 计算器测试
├── pyproject.toml        # 项目配置
├── uv.lock               # 依赖锁定
├── .python-version       # Python 版本
└── README.md
```

## 模块说明

### `task.calculate`

提供 `Calculator` 类，支持：

- `add(a, b)`：加法
- `sub(a, b)`：减法
- `mul(a, b)`：乘法（支持数字、矩阵、混合）
- `div(a, b)`：除法
- `int_div(a, b)`：取整除法
- `mod(a, b)`：取余
- `pow(a, b)`：幂运算（矩阵整数次幂、0 次幂为单位矩阵）

支持数字与 `numpy` 矩阵混合运算，非法组合会抛出 `TypeError`。

用法示例：

```python
from task import calculate

calc = calculate.Calculator()
print(calc.add(1, 2))       # 3
print(calc.mul(2, 3))       # 6
```
