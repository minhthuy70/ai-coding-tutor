'use client';

import React, { useState, useEffect } from 'react';
import {
  X,
  User,
  Award,
  Flame,
  Trophy,
  Zap,
  ShieldCheck,
  Brain,
  Moon,
  Target,
  Code2,
  GraduationCap,
  Sparkles,
  CheckCircle2,
  Lock,
  Edit2,
  Save
} from 'lucide-react';

interface AchievementBadge {
  id: string;
  name: string;
  description: string;
  icon: React.ReactNode;
  isUnlocked: boolean;
  unlockedAt?: string;
  category: 'Thuật toán' | 'Kỷ luật' | 'Chất lượng code';
}

interface UserProfileModalProps {
  isOpen: boolean;
  onClose: () => void;
  solvedCount: number;
  userRole: 'student' | 'instructor';
  onRoleChange: (role: 'student' | 'instructor') => void;
  onOpenRoadmap?: () => void;
  onOpenProblemSet?: () => void;
}

export const UserProfileModal: React.FC<UserProfileModalProps> = ({
  isOpen,
  onClose,
  solvedCount,
  userRole,
  onRoleChange,
  onOpenRoadmap,
  onOpenProblemSet,
}) => {
  // Profile state from localStorage
  const [fullName, setFullName] = useState('Nguyễn Văn A');
  const [studentId, setStudentId] = useState('2111001');
  const [university, setUniversity] = useState('ĐH Bách Khoa TP.HCM (HCMUT)');
  const [favoriteLang, setFavoriteLang] = useState('Python 3.11');
  const [isEditing, setIsEditing] = useState(false);

  // Load from localStorage on mount
  useEffect(() => {
    try {
      const savedName = localStorage.getItem('ai_tutor_user_fullname');
      if (savedName) setFullName(savedName);
      const savedId = localStorage.getItem('ai_tutor_user_studentid');
      if (savedId) setStudentId(savedId);
      const savedUni = localStorage.getItem('ai_tutor_user_uni');
      if (savedUni) setUniversity(savedUni);
      const savedLang = localStorage.getItem('ai_tutor_user_lang');
      if (savedLang) setFavoriteLang(savedLang);
    } catch {}
  }, []);

  const handleSaveProfile = () => {
    try {
      localStorage.setItem('ai_tutor_user_fullname', fullName);
      localStorage.setItem('ai_tutor_user_studentid', studentId);
      localStorage.setItem('ai_tutor_user_uni', university);
      localStorage.setItem('ai_tutor_user_lang', favoriteLang);
    } catch {}
    setIsEditing(false);
  };

  // Calculate XP & Level
  // Each solved problem gives 50 XP, plus 150 base XP for completed lessons
  const totalXp = 150 + solvedCount * 50;
  const currentLevel = Math.min(5, Math.floor(totalXp / 150) + 1);
  const nextLevelXp = currentLevel * 150;
  const currentLevelProgress = Math.min(100, Math.round(((totalXp % 150) / 150) * 100));

  const levelTitles: Record<number, string> = {
    1: 'Tập Sự Lập Trình (Novice Coder)',
    2: 'Thuật Toán Sư Cấp 1 (Algorithm Apprentice)',
    3: 'Chuyên Gia Cấu Trúc Dữ Liệu (Data Structures Specialist)',
    4: 'Kiện Tướng LeetCode (LeetCode Master)',
    5: 'Đại Tôn Sư Giải Thuật (Grandmaster of Algorithms)',
  };

  // Badges list
  const badges: AchievementBadge[] = [
    {
      id: 'badge-01',
      name: 'First Blood (Chiến Công Đầu)',
      description: 'Giải thành công bài toán thuật toán đầu tiên trong Sandbox.',
      icon: <Trophy className="h-5 w-5 text-amber-500" />,
      isUnlocked: solvedCount >= 1,
      unlockedAt: '12/10/2026',
      category: 'Thuật toán',
    },
    {
      id: 'badge-02',
      name: 'Speed Demon (Tốc Độ Bàn Thờ)',
      description: 'Chạy thuật toán với thời gian thực thi dưới 30ms trong Sandbox.',
      icon: <Zap className="h-5 w-5 text-sky-400" />,
      isUnlocked: true,
      unlockedAt: '14/10/2026',
      category: 'Thuật toán',
    },
    {
      id: 'badge-03',
      name: 'Socratic Thinker (Tư Duy Socratic)',
      description: 'Mở khóa gợi ý cấp 1 & 2 để tự tìm lời giải mà không xem code mẫu.',
      icon: <Brain className="h-5 w-5 text-purple-400" />,
      isUnlocked: true,
      unlockedAt: '15/10/2026',
      category: 'Kỷ luật',
    },
    {
      id: 'badge-04',
      name: 'Clean Coder (Mã Nguồn Chuẩn Mực)',
      description: 'Đạt điểm tối đa 100/100 trên trình soát lỗi PEP 8 & Clean Code.',
      icon: <ShieldCheck className="h-5 w-5 text-emerald-400" />,
      isUnlocked: true,
      unlockedAt: '16/10/2026',
      category: 'Chất lượng code',
    },
    {
      id: 'badge-05',
      name: 'Bug Hunter (Thợ Săn Bug)',
      description: 'Sửa thành công test case FAILED trở thành 100% PASSED.',
      icon: <Sparkles className="h-5 w-5 text-rose-400" />,
      isUnlocked: solvedCount >= 1,
      unlockedAt: 'Hôm nay',
      category: 'Thuật toán',
    },
    {
      id: 'badge-06',
      name: 'Night Owl (Cú Đêm Lập Trình)',
      description: 'Thực hiện code và trò chuyện với AI gia sư trong khung giờ đêm khuya.',
      icon: <Moon className="h-5 w-5 text-indigo-400" />,
      isUnlocked: true,
      unlockedAt: 'Hôm nay',
      category: 'Kỷ luật',
    },
    {
      id: 'badge-07',
      name: 'Algorithm Master (Đại Cao Thủ)',
      description: 'Giải quyết toàn bộ 8 bài toán kinh điển trong Đấu trường LeetCode.',
      icon: <Award className="h-5 w-5 text-amber-400" />,
      isUnlocked: solvedCount >= 8,
      category: 'Thuật toán',
    },
    {
      id: 'badge-08',
      name: '7-Day Streak (Kỷ Luật Thép)',
      description: 'Duy trì học tập và giải bài liên tục trong 7 ngày.',
      icon: <Flame className="h-5 w-5 text-orange-500" />,
      isUnlocked: true,
      unlockedAt: '17/10/2026',
      category: 'Kỷ luật',
    },
  ];

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75 backdrop-blur-md animate-in fade-in duration-200">
      <div className="flex flex-col w-full max-w-4xl h-[90vh] bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl overflow-hidden animate-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="px-6 py-4.5 border-b border-slate-200 dark:border-slate-800 bg-gradient-to-r from-amber-50/60 via-white to-purple-50/30 dark:from-slate-900 dark:via-slate-900 dark:to-purple-950/20 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-tr from-amber-500 to-purple-600 text-white shadow-md shadow-amber-500/25">
              <User className="h-6 w-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-black text-slate-900 dark:text-white tracking-tight">
                  Hồ Sơ Học Viên & Hệ Thống Danh Hiệu
                </h2>
                <span className="rounded-full bg-amber-100 dark:bg-amber-900/60 px-2.5 py-0.5 text-[10px] font-extrabold text-amber-700 dark:text-amber-300">
                  Level {currentLevel} • {totalXp} XP
                </span>
              </div>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Theo dõi cấp độ thành thạo thuật toán, huy hiệu thành tích và quản lý vai trò người dùng
              </p>
            </div>
          </div>

          <button
            type="button"
            onClick={onClose}
            className="rounded-2xl p-2 text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          
          {/* Top Row: User Card & Role Switcher */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            
            {/* User Profile Info Card */}
            <div className="md:col-span-2 p-5 rounded-2xl bg-slate-50/80 dark:bg-slate-800/40 border border-slate-200/80 dark:border-slate-800 relative">
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3.5">
                  <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-tr from-blue-600 to-purple-600 text-white font-black text-xl shadow-md shadow-blue-500/20">
                    {fullName.split(' ').slice(-1)[0][0]}
                  </div>
                  <div>
                    {isEditing ? (
                      <div className="space-y-1.5">
                        <input
                          type="text"
                          value={fullName}
                          onChange={(e) => setFullName(e.target.value)}
                          className="px-2 py-0.5 rounded bg-white dark:bg-slate-900 border text-sm font-bold text-slate-900 dark:text-white"
                          placeholder="Họ và tên..."
                        />
                        <input
                          type="text"
                          value={studentId}
                          onChange={(e) => setStudentId(e.target.value)}
                          className="block px-2 py-0.5 rounded bg-white dark:bg-slate-900 border text-xs text-slate-500"
                          placeholder="MSSV..."
                        />
                      </div>
                    ) : (
                      <>
                        <h3 className="text-base font-black text-slate-900 dark:text-white">
                          {fullName}
                        </h3>
                        <p className="text-xs text-slate-400 font-mono mt-0.5">
                          MSSV: {studentId} • {university}
                        </p>
                      </>
                    )}
                    <div className="flex items-center gap-2 mt-1.5">
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-100 dark:bg-blue-900/60 text-blue-700 dark:text-blue-300">
                        {favoriteLang}
                      </span>
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 flex items-center gap-1">
                        <Flame className="h-3 w-3 text-orange-500" />
                        <span>Streak: 7 ngày</span>
                      </span>
                    </div>
                  </div>
                </div>

                <button
                  type="button"
                  onClick={() => {
                    if (isEditing) handleSaveProfile();
                    else setIsEditing(true);
                  }}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-xs font-bold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                >
                  {isEditing ? <Save className="h-3.5 w-3.5 text-blue-500" /> : <Edit2 className="h-3.5 w-3.5" />}
                  <span>{isEditing ? 'Lưu' : 'Sửa'}</span>
                </button>
              </div>

              {/* Level Progress Bar */}
              <div className="pt-2 border-t border-slate-200/60 dark:border-slate-800">
                <div className="flex items-center justify-between text-xs font-bold mb-1.5">
                  <span className="text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                    <Trophy className="h-3.5 w-3.5 text-amber-500" />
                    <span>Cấp bậc: {levelTitles[currentLevel]}</span>
                  </span>
                  <span className="font-mono text-blue-600 dark:text-blue-400">
                    {totalXp} / {nextLevelXp} XP
                  </span>
                </div>
                <div className="w-full h-2.5 rounded-full bg-slate-200 dark:bg-slate-700 overflow-hidden">
                  <div
                    className="h-full bg-gradient-to-r from-blue-500 via-indigo-500 to-purple-600 rounded-full transition-all duration-500"
                    style={{ width: `${currentLevelProgress}%` }}
                  />
                </div>
              </div>
            </div>

            {/* Role Switcher Card */}
            <div className="p-5 rounded-2xl bg-slate-50/80 dark:bg-slate-800/40 border border-slate-200/80 dark:border-slate-800 flex flex-col justify-between">
              <div>
                <span className="text-[11px] font-black uppercase tracking-wider text-slate-400 block mb-1">
                  Chế Độ & Vai Trò Hệ Thống
                </span>
                <h4 className="text-sm font-bold text-slate-900 dark:text-white mb-2">
                  {userRole === 'instructor' ? 'Chế độ: Giảng Viên / Trợ Giảng' : 'Chế độ: Học Viên (Sinh Viên)'}
                </h4>
                <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
                  {userRole === 'instructor'
                    ? 'Mở khóa toàn quyền truy cập Bảng điểm tự động, xuất tệp CSV và tạo bài tập LeetCode mới.'
                    : 'Chế độ học viên tập trung giải bài tập, tích lũy điểm kinh nghiệm XP và nhận gợi ý Socratic.'}
                </p>
              </div>

              <div className="pt-3">
                <div className="flex items-center rounded-xl bg-slate-200/70 dark:bg-slate-900 p-1">
                  <button
                    type="button"
                    onClick={() => onRoleChange('student')}
                    className={`flex-1 py-1.5 rounded-lg text-xs font-bold transition flex items-center justify-center gap-1.5 ${
                      userRole === 'student'
                        ? 'bg-white dark:bg-slate-800 text-blue-600 dark:text-blue-400 shadow-xs'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                    }`}
                  >
                    <User className="h-3.5 w-3.5" />
                    <span>Học Viên</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => onRoleChange('instructor')}
                    className={`flex-1 py-1.5 rounded-lg text-xs font-bold transition flex items-center justify-center gap-1.5 ${
                      userRole === 'instructor'
                        ? 'bg-white dark:bg-slate-800 text-blue-600 dark:text-blue-400 shadow-xs'
                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                    }`}
                  >
                    <GraduationCap className="h-3.5 w-3.5" />
                    <span>Giảng Viên</span>
                  </button>
                </div>
              </div>
            </div>

          </div>

          {/* Badges Showcase Section */}
          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Award className="h-5 w-5 text-amber-500" />
                <h3 className="text-sm font-black text-slate-900 dark:text-white">
                  Bộ Sưu Tập Huy Hiệu Vinh Danh ({badges.filter(b => b.isUnlocked).length} / {badges.length})
                </h3>
              </div>
              <span className="text-xs text-slate-400 font-medium">
                Hoàn thành thử thách để mở khóa huy hiệu
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
              {badges.map((badge) => (
                <div
                  key={badge.id}
                  className={`p-3.5 rounded-2xl border transition-all ${
                    badge.isUnlocked
                      ? 'bg-white dark:bg-slate-800/80 border-slate-200 dark:border-slate-700 shadow-xs'
                      : 'bg-slate-50/50 dark:bg-slate-950/20 border-slate-200/50 dark:border-slate-800/40 opacity-55'
                  }`}
                >
                  <div className="flex items-center justify-between mb-2">
                    <div className={`flex h-10 w-10 items-center justify-center rounded-xl ${
                      badge.isUnlocked
                        ? 'bg-slate-100 dark:bg-slate-700 shadow-xs'
                        : 'bg-slate-200/60 dark:bg-slate-800 text-slate-400'
                    }`}>
                      {badge.isUnlocked ? badge.icon : <Lock className="h-4 w-4 text-slate-400" />}
                    </div>
                    {badge.isUnlocked && (
                      <span className="text-[10px] font-extrabold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/80 px-2 py-0.5 rounded-full flex items-center gap-1">
                        <CheckCircle2 className="h-3 w-3" />
                        <span>Đạt</span>
                      </span>
                    )}
                  </div>

                  <h4 className="text-xs font-bold text-slate-900 dark:text-white mb-1">
                    {badge.name}
                  </h4>
                  <p className="text-[11px] text-slate-500 dark:text-slate-400 leading-snug">
                    {badge.description}
                  </p>
                </div>
              ))}
            </div>
          </div>

          {/* Quick Learning Stats */}
          <div className="p-4 rounded-2xl bg-gradient-to-r from-blue-50/70 via-indigo-50/40 to-purple-50/50 dark:from-slate-950/60 dark:via-indigo-950/20 dark:to-slate-950/60 border border-blue-200/70 dark:border-slate-800 flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-6 text-xs">
              <div>
                <span className="text-slate-400 block text-[11px]">Bài tập đã giải:</span>
                <span className="font-extrabold text-slate-900 dark:text-white text-sm">
                  {solvedCount} / 8 bài LeetCode
                </span>
              </div>
              <div>
                <span className="text-slate-400 block text-[11px]">Tổng kinh nghiệm:</span>
                <span className="font-extrabold text-blue-600 dark:text-blue-400 text-sm">
                  {totalXp} XP
                </span>
              </div>
              <div>
                <span className="text-slate-400 block text-[11px]">Độ chính xác:</span>
                <span className="font-extrabold text-emerald-600 dark:text-emerald-400 text-sm">
                  92.5%
                </span>
              </div>
            </div>

            <div className="flex items-center gap-2">
              {onOpenProblemSet && (
                <button
                  type="button"
                  onClick={() => {
                    onClose();
                    onOpenProblemSet();
                  }}
                  className="px-3.5 py-1.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold transition shadow-md shadow-blue-500/20"
                >
                  Đến Đấu Trường Giải Bài
                </button>
              )}
            </div>
          </div>

        </div>

      </div>
    </div>
  );
};
