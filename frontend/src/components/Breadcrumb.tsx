'use client';

import React from 'react';
import { ChevronRight, Home } from 'lucide-react';

export interface BreadcrumbItem {
  label: string;
  href?: string;
  active?: boolean;
}

interface BreadcrumbProps {
  items?: BreadcrumbItem[];
}

export const Breadcrumb: React.FC<BreadcrumbProps> = ({
  items = [
    { label: 'Dashboard', href: '#', active: false },
    { label: 'System Overview', active: true },
  ],
}) => {
  return (
    <nav aria-label="Breadcrumb" className="mb-6 flex items-center gap-1.5 text-xs text-slate-500">
      <a
        href="#"
        className="flex items-center gap-1 rounded px-1.5 py-1 text-slate-600 transition-colors hover:bg-slate-200/60 hover:text-slate-900"
      >
        <Home className="h-3.5 w-3.5" />
        <span className="sr-only">Home</span>
      </a>

      {items.map((item, index) => (
        <React.Fragment key={index}>
          <ChevronRight className="h-3 w-3 text-slate-400 shrink-0" />
          {item.active ? (
            <span className="font-semibold text-indigo-700 px-1.5 py-0.5 rounded bg-indigo-50/80">
              {item.label}
            </span>
          ) : (
            <a
              href={item.href || '#'}
              className="rounded px-1.5 py-1 text-slate-600 transition-colors hover:bg-slate-200/60 hover:text-slate-900"
            >
              {item.label}
            </a>
          )}
        </React.Fragment>
      ))}
    </nav>
  );
};
