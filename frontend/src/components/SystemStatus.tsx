'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { 
  getHealthStatus, 
  HealthStatusResponse 
} from '../lib/api';
import { 
  CheckCircle2, 
  XCircle, 
  AlertTriangle, 
  RefreshCw, 
  Server, 
  Database, 
  Cpu, 
  Monitor 
} from 'lucide-react';

export const SystemStatus: React.FC = () => {
  const [health, setHealth] = useState<HealthStatusResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [lastUpdated, setLastUpdated] = useState<Date | null>(null);
  const [isClientReady, setIsClientReady] = useState<boolean>(false);

  const fetchStatus = useCallback(async () => {
    setLoading(true);
    try {
      const data = await getHealthStatus();
      setHealth(data);
    } catch {
      setHealth({
        status: 'error',
        database: 'disconnected',
        redis: 'disconnected',
      });
    } finally {
      setLoading(false);
      setLastUpdated(new Date());
    }
  }, []);

  useEffect(() => {
    setIsClientReady(true);
    fetchStatus();
    // Auto-refresh every 10 seconds
    const interval = setInterval(fetchStatus, 10000);
    return () => clearInterval(interval);
  }, [fetchStatus]);

  const renderBadge = (statusStr: string, isHealthy: boolean) => {
    if (loading && !health) {
      return (
        <span className="inline-flex items-center gap-1.5 rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-600">
          <RefreshCw className="h-3.5 w-3.5 animate-spin" />
          Checking...
        </span>
      );
    }

    if (isHealthy) {
      return (
        <span className="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-3 py-1 text-xs font-semibold text-emerald-700 ring-1 ring-inset ring-emerald-600/20">
          <CheckCircle2 className="h-3.5 w-3.5 text-emerald-600" />
          Connected
        </span>
      );
    }

    return (
      <span className="inline-flex items-center gap-1.5 rounded-full bg-rose-50 px-3 py-1 text-xs font-semibold text-rose-700 ring-1 ring-inset ring-rose-600/20">
        <XCircle className="h-3.5 w-3.5 text-rose-600" />
        {statusStr || 'Disconnected'}
      </span>
    );
  };

  const isBackendHealthy = health?.status === 'ok';
  const isDbHealthy = health?.database?.toLowerCase() === 'connected';
  const isRedisHealthy = health?.redis?.toLowerCase() === 'connected';

  const services = [
    {
      name: 'Frontend (Next.js)',
      description: 'Web UI & SSR Client Layer',
      icon: Monitor,
      status: 'Connected',
      isHealthy: isClientReady,
    },
    {
      name: 'Backend (FastAPI)',
      description: 'Asynchronous Core REST API',
      icon: Server,
      status: isBackendHealthy ? 'Connected' : 'Disconnected',
      isHealthy: isBackendHealthy,
    },
    {
      name: 'PostgreSQL 15',
      description: 'Primary Relational Database',
      icon: Database,
      status: health?.database || 'Disconnected',
      isHealthy: isDbHealthy,
    },
    {
      name: 'Redis 7',
      description: 'In-Memory Cache & Message Broker',
      icon: Cpu,
      status: health?.redis || 'Disconnected',
      isHealthy: isRedisHealthy,
    },
  ];

  const allHealthy = isClientReady && isBackendHealthy && isDbHealthy && isRedisHealthy;

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between border-b border-slate-100 pb-5">
        <div>
          <div className="flex items-center gap-2">
            <h2 className="text-xl font-bold text-slate-900">System Status</h2>
            {allHealthy ? (
              <span className="rounded-md bg-emerald-100 px-2 py-0.5 text-xs font-medium text-emerald-800">
                All Systems Operational
              </span>
            ) : (
              <span className="rounded-md bg-amber-100 px-2 py-0.5 text-xs font-medium text-amber-800">
                Degraded / Initializing
              </span>
            )}
          </div>
          <p className="mt-1 text-sm text-slate-500">
            Real-time connection verification with Day 1 infrastructure stack.
          </p>
        </div>

        <div className="flex items-center gap-3">
          {lastUpdated && (
            <span className="text-xs text-slate-400">
              Updated: {lastUpdated.toLocaleTimeString()}
            </span>
          )}
          <button
            onClick={() => fetchStatus()}
            disabled={loading}
            className="inline-flex items-center gap-2 rounded-lg border border-slate-300 bg-white px-3.5 py-2 text-sm font-medium text-slate-700 shadow-sm hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 disabled:opacity-50"
          >
            <RefreshCw className={`h-4 w-4 ${loading ? 'animate-spin text-indigo-600' : ''}`} />
            Refresh
          </button>
        </div>
      </div>

      <div className="mt-6 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {services.map((service, idx) => {
          const Icon = service.icon;
          return (
            <div
              key={idx}
              className="flex flex-col justify-between rounded-lg border border-slate-200/80 bg-slate-50/50 p-4 transition-all hover:border-slate-300 hover:shadow-xs"
            >
              <div>
                <div className="flex items-center justify-between">
                  <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-white shadow-xs border border-slate-200">
                    <Icon className="h-5 w-5 text-slate-700" />
                  </div>
                  {renderBadge(service.status, service.isHealthy)}
                </div>
                <h3 className="mt-3 text-base font-semibold text-slate-900">{service.name}</h3>
                <p className="mt-1 text-xs text-slate-500">{service.description}</p>
              </div>
            </div>
          );
        })}
      </div>

      {health && (
        <div className="mt-6 rounded-lg bg-slate-900 p-4 text-xs font-mono text-slate-200">
          <div className="flex items-center justify-between pb-2 text-slate-400 border-b border-slate-800">
            <span>GET /api/health Response</span>
            <span>HTTP Status: {health.status === 'ok' ? '200 OK' : '503 Service Unavailable'}</span>
          </div>
          <pre className="mt-3 overflow-x-auto text-emerald-400">
            {JSON.stringify(health, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};
