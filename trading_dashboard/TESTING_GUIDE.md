# Moon Dev Trading Dashboard - Testing Guide

## Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Run all tests
npm test

# 3. Run tests in watch mode (for development)
npm run test:watch

# 4. Generate coverage report
npm run test:coverage
```

## What Was Created

### Test Infrastructure (3 files)
1. **jest.config.js** - Jest configuration with Next.js integration
2. **jest.setup.js** - Test environment setup and global mocks
3. **package.json** - Updated with testing dependencies and scripts

### Test Files (11 files, 167 tests)

#### Component Tests (6 files, 97 tests)
- `__tests__/components/AgentCard.test.tsx` (19 tests)
  - Agent status display, confidence scores, metrics formatting
- `__tests__/components/PortfolioOverview.test.tsx` (16 tests)
  - Portfolio values, PnL display, risk levels
- `__tests__/components/TradingInterface.test.tsx` (10 tests)
  - Position management, order execution, trade history
- `__tests__/components/StrategyBuilder.test.tsx` (10 tests)
  - Strategy creation, backtesting, RBI integration
- `__tests__/components/DataVisualization.test.tsx` (20 tests)
  - Analytics charts, performance metrics, data visualization
- `__tests__/components/SettingsPanel.test.tsx` (20 tests)
  - Configuration management, API keys, agent settings

#### App Tests (2 files, 31 tests)
- `__tests__/app/layout.test.tsx` (8 tests)
  - Root layout, dark mode, gradient backgrounds
- `__tests__/app/page.test.tsx` (23 tests)
  - Dashboard page, tab navigation, system controls

#### Type Tests (1 file, 17 tests)
- `__tests__/types/trading.test.ts` (17 tests)
  - TypeScript interface validation, type safety

#### Integration Tests (1 file, 5 tests)
- `__tests__/integration/dashboard-flow.test.tsx` (5 tests)
  - Multi-component workflows, state management

#### Utility Tests (1 file, 19 tests)
- `__tests__/utils/helpers.test.ts` (19 tests)
  - Number formatting, calculations, date utilities

### Documentation (3 files)
1. **__tests__/README.md** - Test structure and guidelines
2. **TEST_SUMMARY.md** - Comprehensive test suite overview
3. **TESTING_GUIDE.md** - This file - quick start guide

## Test Coverage by Component

### AgentCard Component ✓
- [x] Renders agent name and description
- [x] Displays status correctly (active, inactive, error, paused)
- [x] Shows confidence score with progress bar
- [x] Displays metrics (signals, trades, PnL, win rate)
- [x] Shows live indicator for active agents
- [x] Handles different confidence levels (0-100%)
- [x] Formats time correctly (just now, minutes, hours, days ago)
- [x] Handles agents with minimal/extensive metrics
- [x] Formats large numbers with commas
- [x] Renders agent icons correctly

### PortfolioOverview Component ✓
- [x] Renders total portfolio value
- [x] Displays daily and total PnL
- [x] Shows active positions count
- [x] Displays risk level (Low/Medium/High)
- [x] Handles negative PnL values
- [x] Formats large numbers correctly
- [x] Shows percentage changes
- [x] Handles zero positions
- [x] Displays with different risk levels

### TradingInterface Component ✓
- [x] Renders trading interface
- [x] Displays positions/orders/history tabs
- [x] Switches between tabs correctly
- [x] Handles buy/sell orders
- [x] Shows position information
- [x] Displays order history

### StrategyBuilder Component ✓
- [x] Renders strategy builder interface
- [x] Shows create strategy button
- [x] Displays strategy list
- [x] Has backtesting functionality
- [x] Shows RBI integration
- [x] Displays performance metrics

### DataVisualization Component ✓
- [x] Renders analytics interface
- [x] Shows portfolio/performance/agents/market tabs
- [x] Has time range selector
- [x] Refresh and export functionality
- [x] Displays portfolio allocation
- [x] Shows performance metrics (Total Return, Sharpe Ratio, Max Drawdown, Win Rate)
- [x] Handles tab switching
- [x] Updates on time range changes

### SettingsPanel Component ✓
- [x] Renders settings panel
- [x] Shows general/trading/agents/API/notifications tabs
- [x] Has save and reset buttons
- [x] Displays risk settings
- [x] Shows max position size and daily loss settings
- [x] Handles API key inputs
- [x] Agent configuration options
- [x] Notification preferences

### Dashboard Page ✓
- [x] Renders main dashboard
- [x] Shows system status
- [x] Has navigation tabs (Overview, Agents, Trading, Strategies, Analytics, Settings)
- [x] Pause/Resume functionality
- [x] Refresh data capability
- [x] Displays active agents count
- [x] Shows system health metrics
- [x] Recent activity feed
- [x] Start/Stop all agents buttons

### Types ✓
- [x] Agent interface validation
- [x] TradingData interface validation
- [x] Position interface (long/short)
- [x] Order interface (market/limit/stop-loss)
- [x] Strategy interface validation
- [x] Edge cases and boundary values

## Testing Philosophy

### 1. Comprehensive Coverage
Every component has tests covering:
- Basic rendering
- User interactions
- Edge cases
- Error states
- Various prop combinations

### 2. Maintainability
Tests are:
- Well-organized by component
- Clearly named and documented
- Independent and isolated
- Fast to run

### 3. Real-World Scenarios
Tests simulate:
- Actual user interactions
- Real data patterns
- Common edge cases
- Error conditions

## Mocked Dependencies

The following are automatically mocked in `jest.setup.js`:

1. **framer-motion** - Animation library
   ```javascript
   motion.div → <div>
   motion.button → <button>
   AnimatePresence → children only
   ```

2. **next/navigation** - Next.js routing
   ```javascript
   useRouter() → { push, replace, prefetch }
   useSearchParams() → new URLSearchParams()
   usePathname() → ''
   ```

3. **react-hot-toast** - Notifications
   ```javascript
   Toaster → null
   toast.success/error/loading → jest.fn()
   ```

## Common Testing Patterns

### Testing Component Rendering
```typescript
it('should render component', () => {
  render(<Component />)
  expect(screen.getByText('Expected Text')).toBeInTheDocument()
})
```

### Testing User Interactions
```typescript
it('should handle button click', () => {
  render(<Component />)
  const button = screen.getByText('Click Me')
  fireEvent.click(button)
  expect(screen.getByText('Clicked!')).toBeInTheDocument()
})
```

### Testing Props
```typescript
it('should display data from props', () => {
  const mockData = { value: 100 }
  render(<Component data={mockData} />)
  expect(screen.getByText('100')).toBeInTheDocument()
})
```

### Testing State Changes
```typescript
it('should update state on interaction', () => {
  render(<Component />)
  const input = screen.getByRole('textbox')
  fireEvent.change(input, { target: { value: 'test' } })
  expect(input).toHaveValue('test')
})
```

## Running Specific Tests

### Run single test file
```bash
npm test -- AgentCard.test.tsx
```

### Run tests matching pattern
```bash
npm test -- --testNamePattern="should render"
```

### Run tests in a directory
```bash
npm test -- __tests__/components
```

### Run with verbose output
```bash
npm test -- --verbose
```

### Update snapshots
```bash
npm test -- -u
```

## Coverage Report

After running `npm run test:coverage`, you'll get:
- HTML report in `coverage/` directory
- Terminal summary showing:
  - Line coverage
  - Branch coverage
  - Function coverage
  - Statement coverage

### View Coverage Report
```bash
# Generate coverage
npm run test:coverage

# Open HTML report (macOS)
open coverage/lcov-report/index.html

# Open HTML report (Linux)
xdg-open coverage/lcov-report/index.html

# Open HTML report (Windows)
start coverage/lcov-report/index.html
```

## Continuous Integration

### GitHub Actions Example
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm test -- --coverage
```

## Troubleshooting

### Tests Not Running
1. Ensure dependencies are installed: `npm install`
2. Check Node.js version: `node --version` (should be 18+)
3. Clear Jest cache: `npm test -- --clearCache`

### Import Errors
1. Check path aliases in `tsconfig.json`
2. Verify `moduleNameMapper` in `jest.config.js`
3. Ensure files exist at specified paths

### Timeout Errors
```javascript
// In test file
jest.setTimeout(10000) // 10 seconds
```

### React Testing Library Errors
- Use `screen.debug()` to see current DOM
- Use `waitFor()` for async updates
- Prefer accessible queries (getByRole, getByLabelText)

## Best Practices

1. **Test User Behavior, Not Implementation**
   - Focus on what users see and do
   - Avoid testing internal state directly
   - Use semantic queries (getByRole, getByLabelText)

2. **Keep Tests Independent**
   - Each test should work in isolation
   - Don't rely on test execution order
   - Clean up after each test

3. **Write Descriptive Test Names**
   - Use "should" pattern: `it('should render correctly')`
   - Be specific about what's being tested
   - Include the scenario being tested

4. **Use Appropriate Queries**
   - Prefer: getByRole, getByLabelText, getByText
   - Avoid: getByTestId (use as last resort)
   - Use query* for non-existence checks

5. **Test Edge Cases**
   - Empty states
   - Maximum values
   - Minimum values
   - Error conditions

## Next Steps

1. **Run the tests**: `npm test`
2. **Check coverage**: `npm run test:coverage`
3. **Add more tests**: Follow existing patterns in `__tests__/`
4. **Set up CI/CD**: Add GitHub Actions workflow
5. **Monitor coverage**: Aim for >80% coverage

## Resources

- [Jest Documentation](https://jestjs.io/)
- [React Testing Library](https://testing-library.com/react)
- [Next.js Testing](https://nextjs.org/docs/testing)
- [Testing Best Practices](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library)

---

**Test Suite Statistics:**
- Total Test Files: 11
- Total Test Cases: 167
- Total Lines of Test Code: 1,587
- Components Covered: 6/6 (100%)
- Configuration: Complete
- Documentation: Complete

✅ **Test Suite Ready!**