'use client';

import React, { createContext, useContext, useState, useCallback, useEffect, useRef } from 'react';
import { CheckCircle2, XCircle, AlertTriangle, Info, X } from 'lucide-react';

export type ToastType = 'success' | 'error' | 'warning' | 'info';

export interface Toast {
  id: string;
  type: ToastType;
  title: string;
  message?: string;
  duration?: number;
}

interface ConfirmState {
  message: string;
  onConfirm: () => void;
  onCancel?: () => void;
}

interface ToastContextValue {
  showToast: (opts: Omit<Toast, 'id'>) => void;
  confirm: (message: string, onConfirm: () => void, onCancel?: () => void) => void;
}

const ToastContext = createContext<ToastContextValue | null>(null);

export function useToast() {
  const ctx = useContext(ToastContext);
  if (!ctx) throw new Error('useToast must be used inside ToastProvider');
  return ctx;
}

const ICONS: Record<ToastType, React.ReactNode> = {
  success: <CheckCircle2 className="h-4 w-4 text-emerald-500" />,
  error: <XCircle className="h-4 w-4 text-rose-500" />,
  warning: <AlertTriangle className="h-4 w-4 text-amber-500" />,
  info: <Info className="h-4 w-4 text-blue-500" />,
};

const COLORS: Record<ToastType, string> = {
  success: 'border-emerald-200 bg-emerald-50/95 dark:border-emerald-800 dark:bg-emerald-950/95',
  error: 'border-rose-200 bg-rose-50/95 dark:border-rose-800 dark:bg-rose-950/95',
  warning: 'border-amber-200 bg-amber-50/95 dark:border-amber-800 dark:bg-amber-950/95',
  info: 'border-blue-200 bg-blue-50/95 dark:border-blue-800 dark:bg-blue-950/95',
};

const ToastItem: React.FC<{ toast: Toast; onRemove: (id: string) => void }> = ({ toast, onRemove }) => {
  const [visible, setVisible] = useState(false);
  const timerRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    const raf = requestAnimationFrame(() => setVisible(true));
    const duration = toast.duration ?? 4000;
    timerRef.current = setTimeout(() => {
      setVisible(false);
      setTimeout(() => onRemove(toast.id), 300);
    }, duration);
    return () => {
      cancelAnimationFrame(raf);
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [toast.id, toast.duration, onRemove]);

  return (
    <div
      className={`flex items-start gap-3 rounded-xl border px-4 py-3 shadow-lg backdrop-blur-md w-80 transition-all duration-300 ${COLORS[toast.type]} ${
        visible ? 'translate-x-0 opacity-100' : 'translate-x-10 opacity-0'
      }`}
      role="alert"
    >
      <div className="mt-0.5 shrink-0">{ICONS[toast.type]}</div>
      <div className="flex-1 min-w-0">
        <p className="text-xs font-bold text-slate-900 dark:text-slate-100">{toast.title}</p>
        {toast.message && (
          <p className="text-[11px] text-slate-600 dark:text-slate-400 mt-0.5 leading-relaxed">{toast.message}</p>
        )}
      </div>
      <button
        type="button"
        onClick={() => { setVisible(false); setTimeout(() => onRemove(toast.id), 300); }}
        className="shrink-0 rounded-md p-0.5 text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 transition"
        aria-label="Đóng thông báo"
      >
        <X className="h-3.5 w-3.5" />
      </button>
    </div>
  );
};

const ConfirmDialog: React.FC<{ state: ConfirmState; onDone: () => void }> = ({ state, onDone }) => (
  <div
    className="fixed inset-0 z-[200] flex items-center justify-center bg-slate-950/60 backdrop-blur-sm animate-in fade-in duration-150 p-4"
    onClick={() => { state.onCancel?.(); onDone(); }}
  >
    <div
      className="w-full max-w-sm rounded-2xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 p-5 shadow-2xl space-y-4 animate-in zoom-in-95 duration-200"
      onClick={(e) => e.stopPropagation()}
    >
      <div className="flex items-start gap-3">
        <div className="mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-xl bg-amber-100 dark:bg-amber-900/40">
          <AlertTriangle className="h-5 w-5 text-amber-600 dark:text-amber-400" />
        </div>
        <div>
          <p className="font-bold text-sm text-slate-900 dark:text-slate-100">Xác nhận thao tác</p>
          <p className="text-xs text-slate-600 dark:text-slate-400 mt-1 leading-relaxed">{state.message}</p>
        </div>
      </div>
      <div className="flex items-center gap-2 pt-1">
        <button
          type="button"
          onClick={() => { state.onCancel?.(); onDone(); }}
          className="flex-1 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-4 py-2 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-700 transition"
        >
          Hủy
        </button>
        <button
          type="button"
          onClick={() => { state.onConfirm(); onDone(); }}
          className="flex-1 rounded-xl bg-rose-600 hover:bg-rose-700 px-4 py-2 text-xs font-bold text-white transition active:scale-95 shadow-sm"
        >
          Xác nhận
        </button>
      </div>
    </div>
  </div>
);

export const ToastProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [toasts, setToasts] = useState<Toast[]>([]);
  const [confirmState, setConfirmState] = useState<ConfirmState | null>(null);

  const showToast = useCallback((opts: Omit<Toast, 'id'>) => {
    const id = `toast-${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;
    setToasts((prev) => [...prev, { ...opts, id }]);
  }, []);

  const removeToast = useCallback((id: string) => {
    setToasts((prev) => prev.filter((t) => t.id !== id));
  }, []);

  const confirm = useCallback((message: string, onConfirm: () => void, onCancel?: () => void) => {
    setConfirmState({ message, onConfirm, onCancel });
  }, []);

  return (
    <ToastContext.Provider value={{ showToast, confirm }}>
      {children}
      <div className="fixed bottom-5 right-5 z-[100] flex flex-col gap-2 pointer-events-none">
        {toasts.map((t) => (
          <div key={t.id} className="pointer-events-auto">
            <ToastItem toast={t} onRemove={removeToast} />
          </div>
        ))}
      </div>
      {confirmState && (
        <ConfirmDialog state={confirmState} onDone={() => setConfirmState(null)} />
      )}
    </ToastContext.Provider>
  );
};
