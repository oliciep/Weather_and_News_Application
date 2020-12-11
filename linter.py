import pylint.lint
pylint_opts = ['main.py', 'covid.py', 'news.py', 'weather.py', 'time_conversions.py']
pylint.lint.Run(pylint_opts)
