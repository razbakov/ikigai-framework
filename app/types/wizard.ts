export interface WizardProject {
  name: string
  description: string
  techStack: string
}

export interface WizardAgent {
  id: string
  enabled: boolean
  customName: string
  customRole: string
  assignedProjects: string[]
}

export interface WizardState {
  mission: string
  vision: string
  projects: WizardProject[]
  painPoints: string[]
  agents: WizardAgent[]
  selectedSkills: Record<string, string[]>
}

export const PAIN_POINTS = [
  { id: 'inbox-overwhelm', label: 'My inbox controls my day', agents: ['maya'] },
  { id: 'no-daily-routine', label: 'I have no consistent routine', agents: ['maya', 'sage'] },
  { id: 'code-bottleneck', label: "I'm the engineering bottleneck", agents: ['viktor'] },
  { id: 'tech-debt', label: 'Technical debt is piling up', agents: ['viktor'] },
  { id: 'no-content', label: 'I know I should create content but never do', agents: ['luna'] },
  { id: 'seo-invisible', label: 'My products are invisible online', agents: ['luna'] },
  { id: 'no-strategy', label: "I'm building but not sure what to prioritize", agents: ['marco'] },
  { id: 'no-revenue', label: 'None of my projects make money yet', agents: ['marco'] },
  { id: 'burnout', label: "I'm burning out or close to it", agents: ['sage'] },
  { id: 'no-purpose', label: "I've lost sight of why I'm doing this", agents: ['sage'] },
  { id: 'network-cold', label: 'I meet people but never follow up', agents: ['kai'] },
  { id: 'community-empty', label: 'My products have no community', agents: ['kai'] },
  { id: 'too-many-projects', label: "I have too many projects and can't focus", agents: ['marco', 'maya'] },
  { id: 'no-automation', label: 'I do everything manually', agents: ['maya', 'viktor'] },
  { id: 'no-reviews', label: 'I never review my progress', agents: ['maya', 'sage'] },
] as const

export type PainPointId = typeof PAIN_POINTS[number]['id']
