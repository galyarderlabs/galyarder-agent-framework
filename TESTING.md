# 🧪 Testing Galyarder Framework + Dashboard Integration

## Prerequisites

Make sure you have:
- ✅ Node.js 20+ installed
- ✅ pnpm installed (`npm install -g pnpm`)
- ✅ Adapter built (already done)
- ✅ Adapter registered (already done)

## Step 1: Start Dashboard

```bash
cd /home/galyarder/projects/galyarder-framework
pnpm install  # Install dependencies (first time only)
pnpm dev      # Start Dashboard
```

Dashboard will start on: **http://localhost:3100**

## Step 2: Verify Adapter Loaded

Check the server logs for:
```
✅ Loaded external adapter: galyarder_framework
```

Or check in browser console:
```javascript
// Open http://localhost:3100
// Open DevTools (F12)
// Check for adapter in network/console
```

## Step 3: Create a Company

1. Open http://localhost:3100
2. Click "Create Company"
3. Enter company name (e.g., "Test Company")
4. Click "Create"

## Step 4: Create an Agent with Framework Adapter

1. Go to "Agents" page
2. Click "New Agent"
3. Fill in:
   - **Name**: `framework-tester`
   - **Adapter Type**: Select **"Galyarder Framework"** (should appear in dropdown)
   - **Role**: `Test Agent`
4. Click "Create Agent"

## Step 5: Create a Task

1. Go to "Issues" page
2. Click "New Issue"
3. Fill in:
   - **Title**: `Implement user authentication`
   - **Assign to**: `framework-tester`
4. Click "Create"

## Step 6: Verify Execution

The agent should:
1. Pick up the task
2. Route it to appropriate Framework agent (e.g., `elite-developer`)
3. Show execution in transcript

## Expected Results

### ✅ Success Indicators:

1. **Adapter appears in dropdown** when creating agent
2. **Agent created successfully** with type `galyarder_framework`
3. **Task assigned** to Framework agent
4. **Execution logs** show Framework routing

### ❌ If Something Fails:

**Adapter not in dropdown?**
```bash
# Check adapter registration
cat ~/.galyarder/adapter-plugins.json

# Check server logs for errors
# Look for "Failed to load adapter" messages
```

**Agent creation fails?**
```bash
# Check adapter module loads
node -e "import('./packages/adapters/galyarder-framework/dist/server.js').then(console.log)"
```

**Task doesn't execute?**
```bash
# Check Dashboard logs
# Look for execution errors in server console
```

## Quick Test (Without UI)

Test adapter directly:

```bash
cd /home/galyarder/projects/galyarder-framework/packages/adapters/galyarder-framework
node test.js
```

Should show:
```
✅ Loaded 35 agents
✅ Loaded 132 skills
✅ Task routing working
```

## Troubleshooting

### Port 3100 already in use?

```bash
# Kill existing process
pkill -f "node.*server"

# Or use different port
PORT=3101 pnpm dev
```

### Dependencies not installed?

```bash
cd /home/galyarder/projects/galyarder-framework
pnpm install
```

### Adapter not loading?

```bash
# Rebuild adapter
cd packages/adapters/galyarder-framework
npm run build  # or: npx tsc

# Verify build
ls -la dist/server.js
```

## What You Should See

### 1. Server Startup
```
🚀 Starting Galyarder Dashboard...
✅ Database connected
✅ Loaded external adapter: galyarder_framework
🌐 Server running on http://localhost:3100
```

### 2. Agent Creation
```
Agent created: framework-tester
Type: galyarder_framework
Status: Active
```

### 3. Task Execution
```
Task: Implement user authentication
Routed to: elite-developer (Engineering)
Status: In Progress
```

## Next Steps After Testing

Once working:
1. Create more agents for different departments
2. Assign tasks to test routing
3. Verify Framework skills are accessible
4. Test with real workloads

## Need Help?

Check:
- Server logs in terminal
- Browser DevTools console (F12)
- `~/.galyarder/adapter-plugins.json`
- Adapter test: `node packages/adapters/galyarder-framework/test.js`
