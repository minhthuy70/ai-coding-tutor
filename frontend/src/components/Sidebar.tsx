'use client';

import React from 'react';
import { 
  LayoutDashboard, 
  Code2, 
  History, 
  Database, 
  Layers, 
  Settings, 
  ChevronRight,
  Server
} from 'lucide-react';

interface SidebarProps {
  isOpen: boolean;
}

export const Sidebar: React.FC<SidebarProps> = ({ isOpen }) => {
  const navItems = [
    { label: 'System Overview', icon: LayoutDashboard, href: '#', active: true },
    { label: 'Problems (Day 4)', icon: Code2, href: '#', disabled: true },
    { label: 'Submissions (Day 5)', icon: History, href: '#', disabled: true },
    { label: 'Database (Day 2)', icon: Database, href: '#', disabled: true },
    { label: 'Architecture Docs', icon: Layers, href: '#', disabled: true },
    { label: 'Settings', icon: Settings, href: '#', disabled: true },
  ];

  return (
    <aside
      className={`fixed inset-y-0 left-0 top-16 z-20 flex flex-col border-r border-slate-200 bg-white transition-all duration-300 ease-in-out md:static ${
        isOpen ? 'w-64 translate-x-0' : '-translate-x-full md:w-20 md:translate-x-0'
      }`}
    >
      <div className="flex flex-1 flex-col gap-1 p-3">
        <div className="px-3 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400">
          {isOpen ? 'Main Navigation' : '•'}
        </div>
        {navItems.map((item, index) => {
          const Icon = item.icon;
          return (
            <button
              key={index}
              disabled={item.disabled}
              className={`flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-colors ${
                item.active
                  ? 'bg-indigo-50 text-indigo-700'
                  : item.disabled
                  ? 'cursor-not-allowed text-slate-400 opacity-60'
                  : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
              } ${!isOpen && 'justify-center md:px-0'}`}
              title={!isOpen ? item.label : undefined}
            >
              <Icon className="h-5 w-5 shrink-0" />
              {isOpen && <span className="flex-1 text-left">{item.label}</span>}
              {isOpen && item.active && <ChevronRight className="h-4 w-4 text-indigo-500" />}
            </button>
          );
        })}
      </div>

      <div className="border-t border-slate-200 p-3">
        <div
          className={`flex items-center gap-3 rounded-lg bg-slate-50 p-3 text-xs text-slate-600 ${
            !isOpen && 'justify-center p-2'
          }`}
        >
          <Server className="h-4 w-4 shrink-0 text-slate-500" />
          {isOpen && (
            <div className="flex flex-col overflow-hidden">
              <span className="font-semibold text-slate-800">Stack: Microservices</span>
              <span className="truncate text-slate-500">FastAPI + Postgres + Redis</span>
            </div>
          )}
        </div>
      </div>
    </aside>
  );
};
