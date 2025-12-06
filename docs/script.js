// Simple interactive script for the Docs landing page
document.addEventListener('DOMContentLoaded', function () {
  const slider = document.getElementById('scoreSlider');
  const valueEl = document.getElementById('scoreValue');
  const badge = document.getElementById('gradeBadge');

  function gradeForScore(score) {
    if (score >= 90) return ['A+', 'grade-a'];
    if (score >= 80) return ['A', 'grade-a'];
    if (score >= 70) return ['B', 'grade-b'];
    if (score >= 60) return ['C', 'grade-c'];
    if (score >= 50) return ['D', 'grade-d'];
    return ['F', 'grade-f'];
  }

  function updateScore(s) {
    valueEl.textContent = s;
    const [g, cls] = gradeForScore(s);
    badge.textContent = g;
    badge.className = 'score-grade ' + cls;
  }

  slider.addEventListener('input', (e) => updateScore(e.target.value));
  updateScore(slider.value);

  // CLI copy
  const copyBtn = document.getElementById('copyCmd');
  const cmdEl = document.getElementById('cliCmd');
  copyBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(cmdEl.textContent.trim());
      copyBtn.textContent = 'Copied!';
      setTimeout(() => (copyBtn.textContent = 'Copy'), 1500);
    } catch (e) {
      copyBtn.textContent = 'Copy (cmd)';
    }
  });

  // Sample findings
  const findings = [
    { file: 'src/scanner.py', line: 102, type: 'UNSAFE_PICKLE', severity: 'CRITICAL', desc: 'Unpickling untrusted data can execute arbitrary code' },
    { file: 'src/scanner.py', line: 78, type: 'EVAL_USAGE', severity: 'CRITICAL', desc: 'eval() usage' },
    { file: 'src/constants.py', line: 222, type: 'TODO_MARKER', severity: 'INFO', desc: 'TODO markers found' },
    { file: 'src/report_generator.py', line: 45, type: 'UNPINNED_DEPENDENCY', severity: 'MEDIUM', desc: 'Dependency is unpinned' },
    { file: 'src/__main__.py', line: 140, type: 'DEBUG_ENABLED', severity: 'MEDIUM', desc: 'Debug mode enabled in code' },
  ];

  const listEl = document.getElementById('findingsList');
  function renderFindings(filter = 'all') {
    listEl.innerHTML = '';
    const filtered = findings.filter(f => filter === 'all' || f.severity === filter);
    filtered.forEach(f => {
      const li = document.createElement('li');
      li.className = 'finding';
      const left = document.createElement('div');
      left.innerHTML = `<div><strong>${f.type}</strong> <div class="meta">${f.file}:${f.line}</div></div>`;
      const right = document.createElement('div');
      const sev = document.createElement('span');
      sev.className = 'severity-badge ' + (f.severity === 'CRITICAL' ? 'sev-critical' : f.severity === 'HIGH' ? 'sev-high' : f.severity === 'MEDIUM' ? 'sev-medium' : f.severity === 'LOW' ? 'sev-low' : 'sev-low');
      sev.textContent = f.severity;
      right.appendChild(sev);
      li.appendChild(left);
      li.appendChild(right);
      listEl.appendChild(li);
    });
    if (!filtered.length) listEl.innerHTML = '<li class="muted">No findings</li>';
  }
  renderFindings();

  // Filter chips
  document.querySelectorAll('.chip').forEach(ch => {
    ch.addEventListener('click', () => {
      document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      ch.classList.add('active');
      renderFindings(ch.getAttribute('data-sev'));
    });
  });
});
