# UNIVERSAL AUDIT REPORT

Generated: 2025-12-07T13:31:09.368293 UTC
Scanned repo: `c:\workspace\gold_standard`

Score: **5/100**

## Flags Summary
- SECRET: 47
- SUBPROCESS: 8
- TODO_FIXME: 6
- RAW_SQL: 2
- EVAL_EXEC: 1

## File Reports

### .pre-commit-config.yaml

### cortex_memory.json

### cortex_memory.template.json

### db_manager.py
- Flags: RAW_SQL, SECRET
- Matches:
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY AUTOINCREMENT')

### docker-compose.yml

### gui.py
- Flags: SUBPROCESS
- Matches:
  - ('SUBPROCESS', '(subprocess\\.|os\\.system)')

### main.py
- Flags: SECRET, TODO_FIXME
- Matches:
  - ('SECRET', 'API unavailability')
  - ('SECRET', 'API Configuration')
  - ('SECRET', "KEY = 'your-api-key-here")
  - ('TODO_FIXME', '(?i)(TODO|FIXME|HACK|XXX)')

### pyproject.toml

### README.md
- Flags: SECRET, TODO_FIXME
- Matches:
  - ('SECRET', 'KEY=your-key-here')
  - ('SECRET', 'KEY=ntn_xxxxxxxxxxxxx')
  - ('SECRET', 'KEY=your-imgbb-key')
  - ('TODO_FIXME', '(?i)(TODO|FIXME|HACK|XXX)')

### requirements-dev.txt

### requirements.txt

### run.py
- Flags: SUBPROCESS
- Matches:
  - ('SUBPROCESS', '(subprocess\\.|os\\.system)')

### setup.ps1
- Flags: SECRET
- Matches:
  - ('SECRET', 'KEY" -ForegroundColor')

### setup.sh

### twine-draft.txt

### .pytest_cache\README.md

### build\lib\gost\cli.py
- Flags: SUBPROCESS
- Matches:
  - ('SUBPROCESS', '(subprocess\\.|os\\.system)')

### build\lib\gost\core.py
- Flags: SUBPROCESS
- Matches:
  - ('SUBPROCESS', '(subprocess\\.|os\\.system)')

### build\lib\gost\init.py
- Flags: SECRET
- Matches:
  - ('SECRET', 'key\nGEMINI_API_KEY')
  - ('SECRET', 'KEY=your_notion_api_key')
  - ('SECRET', 'KEY=your_key_here')

### build\lib\gost\__init__.py

### build\lib\gost\scripts\__init__.py

### changelog\CHANGELOG.md

### docker\README.md
- Flags: SECRET
- Matches:
  - ('SECRET', 'KEY=your_gemini_api_key')
  - ('SECRET', 'TOKEN=your_notion_token')

### docker\alertmanager\alertmanager.yml

### docker\grafana\dashboards\gold-standard-overview.json

### docker\grafana\provisioning\dashboards\dashboards.yml

### docker\grafana\provisioning\datasources\datasources.yml

### docker\loki\loki.yml

### docker\prometheus\prometheus.yml

### docker\prometheus\rules\alerts.yml

### docker\promtail\promtail.yml

### docs\ARCHITECTURE.md

### docs\CHANGELOG.md

### docs\CONTRIBUTING.md

### docs\GUIDE.md
- Flags: SECRET, TODO_FIXME
- Matches:
  - ('SECRET', 'KEY AUTOINCREMENT')
  - ('SECRET', 'KEY=ntn_xxxxxxxxxxxxx')
  - ('SECRET', 'API connectivity')
  - ('TODO_FIXME', '(?i)(TODO|FIXME|HACK|XXX)')

### docs\LLM_PROVIDERS.md
- Flags: SECRET
- Matches:
  - ('SECRET', 'KEY="YOUR_KEY_HERE')
  - ('SECRET', 'KEY="YOUR_KEY_HERE')
  - ('SECRET', 'API Compatibility')

### docs\output_samples(test).md

### docs\RELEASE.md

### docs\android_blueprint\basic_wireframe.md

### docs\android_blueprint\mvp.md
- Flags: SECRET
- Matches:
  - ('SECRET', 'api: GoldApiService')

### docs\audit_reports\audit_report_2025-12-05.md
- Flags: EVAL_EXEC, TODO_FIXME
- Matches:
  - ('EVAL_EXEC', '\\b(eval|exec)\\(')
  - ('TODO_FIXME', '(?i)(TODO|FIXME|HACK|XXX)')

### docs\audit_reports\post_audit_report_2025-12-05.md
- Flags: RAW_SQL
- Matches:
  - ('RAW_SQL', 'execute\\([^)]*[\'\\"].*[\'\\"]')

### docs\audit_reports\pre_audit_report_2025-12-04.md

### output\chart_urls.json

### output\file_index.json

### output\FILE_INDEX.md

### output\usage_stats.json

### output\archive\20251204024158\chart_urls.json

### output\archive\20251204024158\file_index.json

### output\archive\20251204024158\FILE_INDEX.md

### output\archive\20251204024158\usage_stats.json

### output\archive\20251204024158\reports\FILE_INDEX_2025-12-04_2025-12-04.md

### output\archive\20251204024158\reports\FILE_INDEX_2025-12-04_2025-12-04_2025-12-04_2025-12-04.md

### output\archive\20251204024158\reports\analysis\1Y_2025-12-04.md
- Flags: SECRET
- Matches:
  - ('SECRET', 'key institutional')

### output\archive\20251204024158\reports\analysis\3M_2025-12-04.md

### output\archive\20251204024158\reports\catalysts\Catalysts_2025-12-04.md

### output\archive\20251204024158\reports\economic\EconCalendar_2025-12-04.md

### output\archive\20251204024158\reports\institutional\InstMatrix_2025-12-04.md

### output\archive\20251204024158\reports\journals\Journal_2025-12-04.md

### output\archive\20251204024158\reports\monthly\Monthly_2025-12.md

### output\archive\20251204024158\reports\premarket\PreMarket_2025-12-04.md

### output\archive\20251204024158\research\data_fetch_ACT-20251204-0011_2025-12-04.json

### output\archive\20251204024158\research\data_fetch_ACT-20251204-0012_2025-12-04.json

### output\archive\20251204024158\research\monitor_ACT-20251204-0003_2025-12-04.json

### output\reports\FILE_INDEX_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04_2025-12-04.md

### output\reports\FILE_INDEX_2025-12-05_2025-12-05_2025-12-05.md

### output\reports\FILE_INDEX_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05.md

### output\reports\FILE_INDEX_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05.md

### output\reports\FILE_INDEX_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05.md

### output\reports\FILE_INDEX_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05.md

### output\reports\FILE_INDEX_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05.md

### output\reports\FILE_INDEX_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05_2025-12-05.md

### output\reports\monthly_yearly_report_2025-12-07.md

### output\reports\weekly_rundown_2025-12-06.md

### output\reports\weekly_rundown_2025-12-07.md

### output\reports\analysis\1Y_2025-12-04.md
- Flags: SECRET
- Matches:
  - ('SECRET', 'key institutional')

### output\reports\analysis\1Y_2025-12-05.md
- Flags: SECRET
- Matches:
  - ('SECRET', 'key institutional')

### output\reports\analysis\3M_2025-12-04.md

### output\reports\analysis\3M_2025-12-05.md

### output\reports\catalysts\Catalysts_2025-12-04.md

### output\reports\catalysts\Catalysts_2025-12-05.md

### output\reports\economic\EconCalendar_2025-12-04.md

### output\reports\economic\EconCalendar_2025-12-05.md

### output\reports\institutional\InstMatrix_2025-12-04.md

### output\reports\institutional\InstMatrix_2025-12-05.md

### output\reports\journals\Journal_2025-12-04.md

### output\reports\journals\Journal_2025-12-05.md

### output\reports\monthly\Monthly_2025-12.md

### output\reports\premarket\PreMarket_2025-12-04.md

### output\reports\premarket\PreMarket_2025-12-05.md

### output\research\data_fetch_ACT-20251203-0002_2025-12-05.json

### output\research\data_fetch_ACT-20251203-0002_2025-12-05.md

### output\research\data_fetch_ACT-20251203-0011_2025-12-05.json

### output\research\data_fetch_ACT-20251203-0011_2025-12-05.md

### output\research\data_fetch_ACT-20251203-0012_2025-12-05.json

### output\research\data_fetch_ACT-20251203-0012_2025-12-05.md

### output\research\data_fetch_ACT-20251204-0002_2025-12-05.json

### output\research\data_fetch_ACT-20251204-0002_2025-12-05.md

### output\research\data_fetch_ACT-20251204-0011_2025-12-05.json

### output\research\data_fetch_ACT-20251204-0011_2025-12-05.md

### output\research\data_fetch_ACT-20251204-0012_2025-12-05.json

### output\research\data_fetch_ACT-20251204-0012_2025-12-05.md

### output\research\data_fetch_ACT-20251205-0002_2025-12-05.json

### output\research\data_fetch_ACT-20251205-0002_2025-12-05.md

### output\research\data_fetch_ACT-20251205-0011_2025-12-05.json

### output\research\data_fetch_ACT-20251205-0011_2025-12-05.md

### output\research\data_fetch_ACT-20251205-0012_2025-12-05.json

### output\research\data_fetch_ACT-20251205-0012_2025-12-05.md

### output\research\monitor_ACT-20251203-0003_2025-12-05.json

### output\research\monitor_ACT-20251203-0003_2025-12-05.md

### output\research\monitor_ACT-20251203-0005_2025-12-05.json

### output\research\monitor_ACT-20251203-0005_2025-12-05.md

### output\research\monitor_ACT-20251203-0006_2025-12-05.json

### output\research\monitor_ACT-20251203-0006_2025-12-05.md

### output\research\monitor_ACT-20251203-0018_2025-12-05.json

### output\research\monitor_ACT-20251203-0018_2025-12-05.md

### output\research\monitor_ACT-20251204-0003_2025-12-05.json

### output\research\monitor_ACT-20251204-0003_2025-12-05.md

### output\research\monitor_ACT-20251204-0005_2025-12-05.json

### output\research\monitor_ACT-20251204-0005_2025-12-05.md

### output\research\monitor_ACT-20251204-0006_2025-12-05.json

### output\research\monitor_ACT-20251204-0006_2025-12-05.md

### output\research\monitor_ACT-20251204-0013_2025-12-05.json

### output\research\monitor_ACT-20251204-0013_2025-12-05.md

### output\research\monitor_ACT-20251204-0019_2025-12-05.json

### output\research\monitor_ACT-20251204-0019_2025-12-05.md

### output\research\monitor_ACT-20251204-0027_2025-12-05.json

### output\research\monitor_ACT-20251204-0027_2025-12-05.md

### output\research\monitor_ACT-20251204-0029_2025-12-05.json

### output\research\monitor_ACT-20251204-0029_2025-12-05.md

### output\research\monitor_ACT-20251204-0035_2025-12-05.json

### output\research\monitor_ACT-20251204-0035_2025-12-05.md

### output\research\monitor_ACT-20251204-0038_2025-12-05.json

### output\research\monitor_ACT-20251204-0038_2025-12-05.md

### output\research\monitor_ACT-20251204-0039_2025-12-05.json

### output\research\monitor_ACT-20251204-0039_2025-12-05.md

### output\research\monitor_ACT-20251204-0049_2025-12-05.json

### output\research\monitor_ACT-20251204-0049_2025-12-05.md

### output\research\monitor_ACT-20251205-0003_2025-12-05.json

### output\research\monitor_ACT-20251205-0003_2025-12-05.md

### output\research\monitor_ACT-20251205-0005_2025-12-05.json

### output\research\monitor_ACT-20251205-0005_2025-12-05.md

### output\research\monitor_ACT-20251205-0006_2025-12-05.json

### output\research\monitor_ACT-20251205-0006_2025-12-05.md

### output\research\monitor_ACT-20251205-0019_2025-12-05.json

### output\research\monitor_ACT-20251205-0019_2025-12-05.md

### output\research\research_ACT-20251203-0001_2025-12-05.md

### output\research\research_ACT-20251203-0007_2025-12-05.md

### output\research\research_ACT-20251204-0001_2025-12-05.md
- Flags: SECRET
- Matches:
  - ('SECRET', 'key geopolitical')

### output\research\research_ACT-20251204-0007_2025-12-05.md

### output\research\research_ACT-20251204-0032_2025-12-05.md

### output\research\research_ACT-20251204-0033_2025-12-05.md

### output\research\research_ACT-20251204-0045_2025-12-05.md

### scripts\chart_publisher.py
- Flags: SECRET
- Matches:
  - ('SECRET', 'KEY=your_imgbb_api_key')

### scripts\cleanup_manager.py

### scripts\economic_calendar.py

### scripts\file_organizer.py

### scripts\frontmatter.py

### scripts\get_gold_price.py

### scripts\init_cortex.py

### scripts\insights_engine.py

### scripts\list_gemini_models.py

### scripts\live_analysis.py
- Flags: SECRET
- Matches:
  - ('SECRET', 'key institutional')

### scripts\local_llm.py

### scripts\metrics_server.py

### scripts\notion_debug.py

### scripts\notion_formatter.py

### scripts\notion_publisher.py

### scripts\prevent_secrets.py
- Flags: SECRET, SUBPROCESS
- Matches:
  - ('SECRET', 'aws_secret_access_key')
  - ('SECRET', 'aws_secret_access_key')
  - ('SUBPROCESS', '(subprocess\\.|os\\.system)')

### scripts\pre_market.py
- Flags: TODO_FIXME
- Matches:
  - ('TODO_FIXME', '(?i)(TODO|FIXME|HACK|XXX)')

### scripts\purge.py

### scripts\split_reports.py

### scripts\start_daemon.py
- Flags: SUBPROCESS
- Matches:
  - ('SUBPROCESS', '(subprocess\\.|os\\.system)')

### scripts\task_executor.py

### src\gost\cli.py
- Flags: SUBPROCESS
- Matches:
  - ('SUBPROCESS', '(subprocess\\.|os\\.system)')

### src\gost\core.py
- Flags: SUBPROCESS
- Matches:
  - ('SUBPROCESS', '(subprocess\\.|os\\.system)')

### src\gost\init.py
- Flags: SECRET
- Matches:
  - ('SECRET', 'key\nGEMINI_API_KEY')
  - ('SECRET', 'KEY=your_notion_api_key')
  - ('SECRET', 'KEY=your_key_here')

### src\gost\__init__.py

### src\gost\scripts\__init__.py

### src\gost.egg-info\dependency_links.txt

### src\gost.egg-info\entry_points.txt

### src\gost.egg-info\requires.txt

### src\gost.egg-info\SOURCES.txt

### src\gost.egg-info\top_level.txt

### tests\test_core.py

### tests\test_file_organizer.py

### tests\test_gemini.py
- Flags: SECRET
- Matches:
  - ('SECRET', 'API configuration')
  - ('SECRET', 'KEY == "test-api-key-12345')
  - ('SECRET', 'API connectivity')
  - ('SECRET', 'API connectivity')
  - ('SECRET', 'key="invalid-key-12345')

### tests\test_init_cortex.py

### tests\test_insights.py
- Flags: TODO_FIXME
- Matches:
  - ('TODO_FIXME', '(?i)(TODO|FIXME|HACK|XXX)')

### tests\test_integration.py

### tests\test_split_reports.py

### tests\test_ta_fallback.py
