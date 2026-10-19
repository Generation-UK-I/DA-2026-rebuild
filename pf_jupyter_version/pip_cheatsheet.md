# pip Cheatsheet

## Installation & Upgrade

|Function|Command|
|---|---|
|Install a package|`pip install package_name`|
|Install specific version|`pip install package_name==1.2.3`|
|Install minimum version|`pip install "package_name>=1.2.3"`|
|Install from requirements file|`pip install -r requirements.txt`|
|Install in editable/development mode|`pip install -e .`|
|Upgrade a package|`pip install --upgrade package_name`|
|Upgrade pip itself|`python -m pip install --upgrade pip`|
|Force reinstall|`pip install --force-reinstall package_name`|
|Install without dependencies|`pip install --no-deps package_name`|

## Uninstalling

|Function|Command|
|---|---|
|Uninstall a package|`pip uninstall package_name`|
|Uninstall without confirmation|`pip uninstall -y package_name`|
|Uninstall multiple packages|`pip uninstall pkg1 pkg2 pkg3`|
|Uninstall all packages (use with caution)|`pip freeze \| xargs pip uninstall -y`|

## Listing & Searching

|Function|Command|
|---|---|
|List installed packages|`pip list`|
|List outdated packages|`pip list --outdated`|
|Show package details|`pip show package_name`|
|Search PyPI (deprecated, use web search instead)|`pip search package_name`|
|List packages in requirements format|`pip freeze`|

## Requirements Files

|Function|Command|
|---|---|
|Show cache info|`pip cache info`|
|List cached packages|`pip cache list`|
|Remove all cached wheels|`pip cache purge`|
|Remove specific package from cache|`pip cache remove package_name`|

## Downloading & Wheels

|Function|Command|
|---|---|
|Download package without installing|`pip download package_name`|
|Download to specific directory|`pip download package_name -d ./downloads`|
|Build a wheel|`pip wheel package_name`|
|Install from local wheel|`pip install ./package_name-1.0.0-py3-none-any.whl`|

## Configuration

|Function|Command|
|---|---|
|Show current config|`pip config list`|
|Set global config|`pip config set global.index-url https://pypi.org/simple`|
|Use alternate index|`pip install --index-url https://test.pypi.org/simple/ package_name`|
|Use extra index|`pip install --extra-index-url https://example.com/simple package_name`|

## Useful Flags

|Flag|Description|
|---|---|
|`-U`, `--upgrade`|Upgrade package|
|`-r`, `--requirement`|Install from requirements file|
|`-e`, `--editable`|Editable install|
|`-y`, `--yes`|Skip confirmation|
|`-q`, `--quiet`|Less output|
|`-v`, `--verbose`|More output|
|`--no-cache-dir`|Disable cache|
|`--user`|Install to user site-packages|
|`--dry-run`|Show what would happen|
|`--target DIR`|Install to a specific directory|
|`--pre`|Include pre-release versions|

## Troubleshooting

|Flag|Description|
|---|---|
|Fix broken installs / resolve dependency issues|`pip install --upgrade --force-reinstall package_name`|
|Check for dependency conflicts|`pip check`|
|See why a package is installed (requires pipdeptree)|`pip install pipdeptree` > `pipdeptree`|
|Run pip as module (avoids PATH issues)|`python -m pip install package_name`|

## Virtual Environments (bonus)

|Function|Command|
|---|---|
|Create venv|`python -m venv venv`|
|Activate (Linux/Mac)|`source venv/bin/activate`|
|Activate (Windows)|`venv\Scripts\activate`|
|Deactivate|`deactivate`|
