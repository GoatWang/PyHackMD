# Getting Start
## prerequists
1. Python (version free)
2. HackMD Token: please see [official website](https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fhow-to-issue-an-api-token) to get the token.

## API Interface
1. Get Note list
```python
from PyHackMD import API
from pprint import pprint
api = API('<token>')
data = api.get_note_list()
pprint(data)
```

2. Get Note Content
```python
from PyHackMD import API
from pprint import pprint
api = API('<token>')
data = api.get_note('<note_id>')
pprint(data)
```

3. Create Note
```python
from PyHackMD import API
from pprint import pprint
api = API('<token>')
data = api.create_note(title="Test Create Note")
pprint(data)
```

4. Update Note
```python
from PyHackMD import API
from pprint import pprint
api = API('<token>')
data = api.update_note("<note_id>", content="# Test Update Note")
pprint(data)
```

5. Delete Note
```python
from PyHackMD import API
from pprint import pprint
api = API('<token>')
data = api.delete_note("<note_id>")
pprint(data)
```

6. Get Note Read History
```python
from PyHackMD import API
from pprint import pprint
api = API('<token>')
data = api.get_note_read_history()
pprint(data)
```