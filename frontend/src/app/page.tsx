'use client';

import React, { useState } from 'react';
import { Header } from '../components/Header';
import { Sidebar } from '../components/Sidebar';
import { Breadcrumb } from '../components/Breadcrumb';
import { SystemStatus } from '../components/SystemStatus';
import { 
  Rocket, 
  CheckCircle, 
  Terminal, 
  Server, 
  Layers, 
  GitBranch,
  ShieldAlert
} from 'lucide-react';

export default function HomePage() {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Header onToggleSidebar={() => setSidebarOpen((prev) => !prev)} />

      <div className="flex flex-1">
        <Sidebar isOpen={sidebarOpen} />

        <main className="flex-1 p-6 md:p-8 max-w-7xl mx-auto w-full transition-all">
          {/* Breadcrumb Navigation */}
          <Breadcrumb />

          {/* Welcome Banner */}
          <div className="mb-8 rounded-xl bg-gradient-to-r from-indigo-700 via-indigo-600 to-blue-600 p-6 md:p-8 text-white shadow-md">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
              <div>
                <div className="flex items-center gap-2 text-indigo-100 text-sm font-medium mb-1">
                  <Rocket className="h-4 w-4" />
                  <span>Day 1 Implementation: Monorepo Foundation & Core Infrastructure</span>
                </div>
                <h1 className="text-2xl md:text-3xl font-extrabold tracking-tight">
                  AI-Powered Coding Tutor & Auto-Grader
                </h1>
                <p className="mt-2 text-indigo-100 text-sm md:text-base max-w-2xl">
                  Automated code assessment, execution evidence-grounded analysis, and intelligent Socratic tutoring platform.
                </p>
              </div>

              <div className="flex items-center gap-2 self-start md:self-auto rounded-lg bg-white/10 px-4 py-2 backdrop-blur-xs border border-white/20">
                <GitBranch className="h-4 w-4 text-emerald-300" />
                <span className="text-xs font-semibold uppercase tracking-wider text-white">
                  Sprint Day 1 (01/10/2026)
                </span>
              </div>
            </div>
          </div>

          {/* System Status Dashboard Widget */}
          <div className="mb-8">
            <SystemStatus />
          </div>

          {/* Architecture Overview & Day 1 Scope */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-xs">
              <div className="flex items-center gap-2 text-indigo-600 font-semibold text-base mb-3">
                <Layers className="h-5 w-5" />
                <h3>Day 1 Foundation Scope</h3>
              </div>
              <ul className="space-y-2 text-sm text-slate-600">
                <li className="flex items-start gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 mt-0.5 shrink-0" />
                  <span>Monorepo workspace setup (backend, frontend, sandbox, docs)</span>
                </li>
                <li className="flex items-start gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 mt-0.5 shrink-0" />
                  <span>Docker Compose orchestration with healthchecks</span>
                </li>
                <li className="flex items-start gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 mt-0.5 shrink-0" />
                  <span>FastAPI modular backend with CORS &amp; async connection pools</span>
                </li>
                <li className="flex items-start gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 mt-0.5 shrink-0" />
                  <span>Next.js 14 App Router with Tailwind CSS &amp; dynamic health checker</span>
                </li>
                <li className="flex items-start gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 mt-0.5 shrink-0" />
                  <span>End-to-end communication via <code className="bg-slate-100 px-1 py-0.5 rounded text-indigo-600">/api/health</code></span>
                </li>
              </ul>
            </div>

            <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-xs">
              <div className="flex items-center gap-2 text-indigo-600 font-semibold text-base mb-3">
                <ShieldAlert className="h-5 w-5 text-amber-500" />
                <h3>Scope Constraints (Day 2+ Ahead)</h3>
              </div>
              <p className="text-sm text-slate-500 mb-3">
                Per project plan, the following complex business modules are strictly reserved for subsequent days:
              </p>
              <div className="grid grid-cols-2 gap-2 text-xs text-slate-500">
                <span className="rounded bg-slate-100 px-2 py-1">Day 2: Full DB Schema &amp; Alembic</span>
                <span className="rounded bg-slate-100 px-2 py-1">Day 3: JWT Auth &amp; RBAC</span>
                <span className="rounded bg-slate-100 px-2 py-1">Day 4: Problem Management</span>
                <span className="rounded bg-slate-100 px-2 py-1">Day 5: Monaco Web IDE &amp; Drafts</span>
                <span className="rounded bg-slate-100 px-2 py-1">Week 2: Docker Sandbox Runner</span>
                <span className="rounded bg-slate-100 px-2 py-1">Week 3: Evidence ContextBuilder</span>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}
