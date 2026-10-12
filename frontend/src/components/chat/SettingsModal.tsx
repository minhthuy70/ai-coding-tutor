'use client';

import React, { useEffect, useState } from 'react';
import { X, Sliders, Moon, Sun, Sparkles, Shield, Cpu, Zap, Volume2, VolumeX } from 'lucide-react';
import { ModelSettings } from '@/types/chat';
import { isSoundEnabled, setSoundEnabled } from '@/lib/soundEffects';

interface SettingsModalProps {
  isOpen: boolean;
  onClose: () => void;
  settings: ModelSettings;
  onUpdateSettings: (settings: ModelSettings) => void;
  isDarkMode: boolean;
  onToggleDarkMode: () => void;
}

export const SettingsModal: React.FC<SettingsModalProps> = ({
  isOpen,
  onClose,
  settings,
  onUpdateSettings,
  isDarkMode,
  onToggleDarkMode,
}) => {
  const [soundOn, setSoundOn] = useState<boolean>(() => isSoundEnabled());

  const handleToggleSound = () => {
    const next = !soundOn;
    setSoundOn(next);
    setSoundEnabled(next);
  };
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (isOpen) {
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const personas = [
    {
      id: 'socratic',
      title: 'Trợ giảng Socratic',
      desc: 'Đặt câu hỏi gợi mở, hướng dẫn tư duy từng bước, không đưa trực tiếp code giải sẵn',
      icon: Sparkles,
    },
    {
      id: 'algorithm_expert',
      title: 'Chuyên gia Giải thuật & Big-O',
      desc: 'Tập trung phân tích độ phức tạp O(n), đệ quy, tối ưu bộ nhớ và cấu trúc dữ liệu',
      icon: Zap,
    },
    {
      id: 'strict_reviewer',
      title: 'Rà soát Clean Code',
      desc: 'Đánh giá chuẩn phong cách mã nguồn, PEP 8, phát hiện code smells và lỗ hổng bảo mật',
      icon: Shield,
    },
  ];

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/70 backdrop-blur-xs p-4 animate-in fade-in duration-150"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-lg rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 shadow-2xl space-y-4 max-h-[90vh] overflow-y-auto"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
          <div className="flex items-center gap-2 text-slate-900 dark:text-slate-100 font-bold text-sm">
            <Sliders className="h-4.5 w-4.5 text-blue-600 dark:text-blue-400" />
            <span>Cài đặt &amp; Tùy chỉnh AI</span>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="rounded-lg p-1 text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-700 dark:hover:text-slate-200 transition"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        {/* Theme Setting */}
        <div className="flex items-center justify-between rounded-xl border border-slate-150 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800/60 p-3">
          <div className="flex items-center gap-2.5">
            {isDarkMode ? <Moon className="h-4 w-4 text-blue-500" /> : <Sun className="h-4 w-4 text-amber-500" />}
            <div>
              <p className="text-xs font-bold text-slate-800 dark:text-slate-200">Chế độ hiển thị</p>
              <p className="text-[11px] text-slate-500 dark:text-slate-400">Chuyển đổi giao diện Sáng / Tối</p>
            </div>
          </div>
          <button
            type="button"
            onClick={onToggleDarkMode}
            className={`flex items-center gap-1.5 rounded-lg border px-3 py-1.5 text-xs font-semibold transition ${
              isDarkMode
                ? 'border-blue-600 bg-blue-600/20 text-blue-400 hover:bg-blue-600/30'
                : 'border-slate-300 bg-white text-slate-700 hover:bg-slate-50'
            }`}
          >
            {isDarkMode ? 'Đang bật Tối' : 'Đang bật Sáng'}
          </button>
        </div>

        {/* Sound Effects Setting */}
        <div className="flex items-center justify-between rounded-xl border border-slate-150 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-800/60 p-3">
          <div className="flex items-center gap-2.5">
            {soundOn ? <Volume2 className="h-4 w-4 text-emerald-500" /> : <VolumeX className="h-4 w-4 text-slate-400" />}
            <div>
              <p className="text-xs font-bold text-slate-800 dark:text-slate-200">Hiệu ứng âm thanh</p>
              <p className="text-[11px] text-slate-500 dark:text-slate-400">Âm thanh phản hồi khi gửi tin và sinh code</p>
            </div>
          </div>
          <button
            type="button"
            onClick={handleToggleSound}
            className={`flex items-center gap-1.5 rounded-lg border px-3 py-1.5 text-xs font-semibold transition ${
              soundOn
                ? 'border-emerald-600 bg-emerald-600/20 text-emerald-500 dark:text-emerald-400 hover:bg-emerald-600/30'
                : 'border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-500 hover:bg-slate-50'
            }`}
          >
            {soundOn ? 'Đang bật' : 'Đã tắt'}
          </button>
        </div>

        {/* Persona Presets */}
        <div className="space-y-2">
          <label className="text-xs font-bold text-slate-800 dark:text-slate-200 block">
            Phong cách sư phạm của Trợ giảng AI:
          </label>
          <div className="space-y-2">
            {personas.map((p) => {
              const Icon = p.icon;
              const isSelected = settings.persona === p.id;
              return (
                <div
                  key={p.id}
                  onClick={() => onUpdateSettings({ ...settings, persona: p.id as any })}
                  className={`flex items-start gap-3 rounded-xl border p-3 cursor-pointer transition ${
                    isSelected
                      ? 'border-blue-500 bg-blue-50/40 dark:bg-blue-950/40 ring-1 ring-blue-500/20'
                      : 'border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/50'
                  }`}
                >
                  <div className={`mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-lg ${isSelected ? 'bg-blue-600 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'}`}>
                    <Icon className="h-4 w-4" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-xs font-bold text-slate-900 dark:text-slate-100">{p.title}</p>
                    <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5 leading-relaxed">{p.desc}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Temperature slider */}
        <div className="space-y-2 rounded-xl border border-slate-150 dark:border-slate-800 p-3 bg-slate-50/50 dark:bg-slate-800/40">
          <div className="flex items-center justify-between text-xs font-semibold text-slate-800 dark:text-slate-200">
            <span>Độ sáng tạo (Temperature):</span>
            <span className="font-mono text-blue-600 dark:text-blue-400 font-bold">{settings.temperature.toFixed(2)}</span>
          </div>
          <input
            type="range"
            min="0.0"
            max="1.0"
            step="0.05"
            value={settings.temperature}
            onChange={(e) => onUpdateSettings({ ...settings, temperature: parseFloat(e.target.value) })}
            className="w-full h-1.5 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-600"
          />
          <div className="flex justify-between text-[10px] text-slate-400 dark:text-slate-500">
            <span>Chính xác &amp; Logic (0.0)</span>
            <span>Cân bằng (0.7)</span>
            <span>Sáng tạo (1.0)</span>
          </div>
        </div>

        {/* Max Tokens slider */}
        <div className="space-y-2 rounded-xl border border-slate-150 dark:border-slate-800 p-3 bg-slate-50/50 dark:bg-slate-800/40">
          <div className="flex items-center justify-between text-xs font-semibold text-slate-800 dark:text-slate-200">
            <span>Độ dài phản hồi tối đa (Max Tokens):</span>
            <span className="font-mono text-blue-600 dark:text-blue-400 font-bold">{settings.maxTokens}</span>
          </div>
          <input
            type="range"
            min="512"
            max="4096"
            step="256"
            value={settings.maxTokens}
            onChange={(e) => onUpdateSettings({ ...settings, maxTokens: parseInt(e.target.value) })}
            className="w-full h-1.5 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-600"
          />
          <div className="flex justify-between text-[10px] text-slate-400 dark:text-slate-500">
            <span>Ngắn gọn (512)</span>
            <span>Mặc định (2048)</span>
            <span>Chi tiết (4096)</span>
          </div>
        </div>

        {/* Footer */}
        <div className="pt-2 border-t border-slate-100 dark:border-slate-800 flex justify-end">
          <button
            type="button"
            onClick={onClose}
            className="rounded-xl bg-blue-600 px-4 py-2 text-xs font-semibold text-white hover:bg-blue-700 transition shadow-xs"
          >
            Lưu cài đặt
          </button>
        </div>
      </div>
    </div>
  );
};
