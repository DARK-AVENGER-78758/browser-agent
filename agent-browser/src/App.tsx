import { useState } from 'react';
import axios from 'axios';

function App() {
  const [task, setTask] = useState('');
  const [script, setScript] = useState('');
  const [logs, setLogs] = useState('');
  const [loading, setLoading] = useState(false);

  const handleRunTask = async () => {
    setLoading(true);
    setScript('');
    setLogs('');

    try {
      // Step 1: Generate Script
      const genRes = await axios.post('http://127.0.0.1:8000/generate-script', { task });
      const scriptContent = genRes.data.script;
      const scriptId = genRes.data.script_id;

      setScript(scriptContent);

      // Step 2: Execute Script
      const execRes = await axios.post(`http://127.0.0.1:8000/execute-script/${scriptId}`);
      const logOutput = execRes.data.stdout || execRes.data.stderr;
      setLogs(logOutput || 'Script executed, but no output.');
    } catch (error) {
      console.error(error);
      setLogs('An error occurred while running the task.');
    } finally {
      setLoading(false);
    }
  };

  const handleRunSampleScript = async () => {
    setLoading(true);
    setLogs('');

    try {
      const res = await axios.post('http://127.0.0.1:8000/run-sample-script');
      setLogs(res.data.status);
    } catch (error) {
      console.error(error);
      setLogs('An error occurred while running the sample script.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>AI Browser Automation Agent</h1>
      
      <textarea
        placeholder="Describe your task..."
        value={task}
        onChange={(e) => setTask(e.target.value)}
        style={{ width: '100%', height: '100px', marginBottom: '10px' }}
      />

      <div style={{ marginBottom: '10px' }}>
        <button onClick={handleRunTask} disabled={loading} style={{ marginRight: '10px' }}>
          {loading ? 'Processing...' : 'Run AI Task'}
        </button>

        <button onClick={handleRunSampleScript} disabled={loading}>
          {loading ? 'Processing...' : 'Run Sample Script'}
        </button>
      </div>

      <h2>Generated Script</h2>
      <pre style={{ background: '#f0f0f0', padding: '10px' }}>{script}</pre>

      <h2>Execution Logs</h2>
      <pre style={{ background: '#f0f0f0', padding: '10px' }}>{logs}</pre>
    </div>
  );
}

export default App;
