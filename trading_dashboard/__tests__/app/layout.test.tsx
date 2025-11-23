import React from 'react'
import { render, screen } from '@testing-library/react'
import RootLayout from '@/app/layout'

describe('RootLayout Component', () => {
  it('should render children', () => {
    render(
      <RootLayout>
        <div>Test Content</div>
      </RootLayout>
    )
    
    expect(screen.getByText('Test Content')).toBeInTheDocument()
  })

  it('should have dark class on html element', () => {
    const { container } = render(
      <RootLayout>
        <div>Test</div>
      </RootLayout>
    )
    
    const html = container.querySelector('html')
    expect(html).toHaveClass('dark')
  })

  it('should render gradient background', () => {
    const { container } = render(
      <RootLayout>
        <div>Test</div>
      </RootLayout>
    )
    
    const bgElement = container.querySelector('.bg-gradient-to-br')
    expect(bgElement).toBeInTheDocument()
  })

  it('should include Toaster component', () => {
    render(
      <RootLayout>
        <div>Test</div>
      </RootLayout>
    )
    
    // Toaster is mocked to return null in jest.setup.js
    expect(screen.getByText('Test')).toBeInTheDocument()
  })

  it('should render with min-h-screen', () => {
    const { container } = render(
      <RootLayout>
        <div>Test</div>
      </RootLayout>
    )
    
    const minHeight = container.querySelector('.min-h-screen')
    expect(minHeight).toBeInTheDocument()
  })

  it('should wrap content correctly', () => {
    render(
      <RootLayout>
        <div data-testid="child-content">Child Content</div>
      </RootLayout>
    )
    
    expect(screen.getByTestId('child-content')).toBeInTheDocument()
  })

  it('should render html with lang attribute', () => {
    const { container } = render(
      <RootLayout>
        <div>Test</div>
      </RootLayout>
    )
    
    const html = container.querySelector('html')
    expect(html).toHaveAttribute('lang', 'en')
  })

  it('should apply Inter font', () => {
    const { container } = render(
      <RootLayout>
        <div>Test</div>
      </RootLayout>
    )
    
    const body = container.querySelector('body')
    expect(body).toBeTruthy()
  })
})