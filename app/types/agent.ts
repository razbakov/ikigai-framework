export interface AgentDefinition {
  id: string
  name: string
  role: string
  icon: string
  avatar: string
  personality: string
  color: string
  description: string
  responsibilities: string[]
  s3Domain: string
  defaultSkills: string[]
  painPointMatches: string[]
}

export const AGENTS: AgentDefinition[] = [
  {
    id: 'maya',
    name: 'Maya',
    role: 'Chief of Staff',
    icon: 'lucide:clipboard-list',
    avatar: '/images/agents/maya.png',
    personality: 'ISTJ',
    color: 'maya',
    description: 'Maya keeps everything running. She owns your daily rhythm, manages your inbox, coordinates between agents, and ensures nothing falls through the cracks.',
    responsibilities: [
      'Daily standup and check-in coordination',
      'Inbox processing and GTD workflow',
      'Cross-agent task delegation and follow-up',
    ],
    s3Domain: 'Operations & Coordination',
    defaultSkills: ['daily-review', 'inbox-processing', 'weekly-review', 'meeting-prep'],
    painPointMatches: ['inbox-overwhelm', 'no-daily-routine', 'too-many-projects', 'no-automation', 'no-reviews'],
  },
  {
    id: 'viktor',
    name: 'Viktor',
    role: 'CTO',
    icon: 'lucide:code',
    avatar: '/images/agents/viktor.png',
    personality: 'INTJ',
    color: 'viktor',
    description: 'Viktor handles the technical side. He architects solutions, writes code, manages deployments, and keeps your tech stack healthy and your codebase clean.',
    responsibilities: [
      'Architecture decisions and code reviews',
      'CI/CD pipeline and deployment management',
      'Technical debt tracking and resolution',
    ],
    s3Domain: 'Engineering & Architecture',
    defaultSkills: ['code-review', 'deploy', 'tech-debt-audit', 'bug-triage'],
    painPointMatches: ['code-bottleneck', 'tech-debt', 'no-automation'],
  },
  {
    id: 'luna',
    name: 'Luna',
    role: 'Head of Content & Growth',
    icon: 'lucide:pen-tool',
    avatar: '/images/agents/luna.png',
    personality: 'ENFP',
    color: 'luna',
    description: 'Luna turns your ideas into content that reaches people. She writes blog posts, manages social media, optimizes for SEO, and builds your public presence.',
    responsibilities: [
      'Blog posts, newsletters, and social media',
      'SEO optimization and content calendar',
      'Brand voice and messaging consistency',
    ],
    s3Domain: 'Content & Growth',
    defaultSkills: ['blog-post', 'social-media', 'seo-audit', 'content-calendar'],
    painPointMatches: ['no-content', 'seo-invisible'],
  },
  {
    id: 'marco',
    name: 'Marco',
    role: 'Head of Strategy & Business',
    icon: 'lucide:target',
    avatar: '/images/agents/marco.png',
    personality: 'ENTJ',
    color: 'marco',
    description: 'Marco ensures you are building the right things. He defines OKRs, evaluates business models, tracks metrics, and keeps your portfolio focused on what matters.',
    responsibilities: [
      'OKR setting and quarterly planning',
      'Business model validation and pricing',
      'Competitive analysis and market research',
    ],
    s3Domain: 'Strategy & Business',
    defaultSkills: ['okr-review', 'market-research', 'pricing-strategy', 'competitor-analysis'],
    painPointMatches: ['no-strategy', 'no-revenue', 'too-many-projects'],
  },
  {
    id: 'sage',
    name: 'Sage',
    role: 'Personal Coach',
    icon: 'lucide:heart',
    avatar: '/images/agents/sage.png',
    personality: 'INFJ',
    color: 'sage',
    description: 'Sage watches out for you as a human. She tracks your energy, flags burnout risk, helps you reconnect with purpose, and maintains the balance between ambition and wellbeing.',
    responsibilities: [
      'Energy and burnout monitoring',
      'Purpose and motivation alignment',
      'Health habits and routine coaching',
    ],
    s3Domain: 'Personal Development & Wellbeing',
    defaultSkills: ['check-in', 'journal-prompt', 'energy-audit', 'life-assessment'],
    painPointMatches: ['burnout', 'no-purpose', 'no-daily-routine', 'no-reviews'],
  },
  {
    id: 'kai',
    name: 'Kai',
    role: 'Community & Partnerships',
    icon: 'lucide:users',
    avatar: '/images/agents/kai.png',
    personality: 'ESFJ',
    color: 'kai',
    description: 'Kai builds your network and nurtures your community. He manages contacts, follows up after events, runs community engagement, and opens doors to partnerships.',
    responsibilities: [
      'Contact management and follow-ups',
      'Community engagement and events',
      'Partnership outreach and relationship nurturing',
    ],
    s3Domain: 'Community & Partnerships',
    defaultSkills: ['contact-enrichment', 'follow-up', 'community-pulse', 'event-planning'],
    painPointMatches: ['network-cold', 'community-empty'],
  },
]
