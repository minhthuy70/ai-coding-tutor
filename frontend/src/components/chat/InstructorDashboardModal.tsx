'use client';

import React, { useState, useMemo } from 'react';
import {
  X,
  GraduationCap,
  Users,
  CheckCircle2,
  AlertCircle,
  Download,
  Search,
  Filter,
  Plus,
  Trash2,
  Edit3,
  BookOpen,
  Award,
  Sparkles,
  TrendingUp,
  FileSpreadsheet,
  Clock,
  ChevronRight,
  ShieldCheck,
  Send
} from 'lucide-react';
import { PROBLEMS_DATA, CodingProblem } from './ProblemSetModal';

interface StudentGradeRecord {
  id: string;
  studentId: string;
  fullName: string;
  email: string;
  avatarBg: string;
  submissionsCount: number;
  lastActive: string;
  // Scores for each problem id (0 to 100)
  scores: Record<string, number>;
  totalScore: number;
  status: 'Xuất sắc' | 'Đạt' | 'Cần trợ giúp';
}

interface InstructorDashboardModalProps {
  isOpen: boolean;
  onClose: () => void;
  onOpenProblemSet?: () => void;
  onPublishAssignment?: (problem: CodingProblem) => void;
}

// Mock student roster for CS102 - Data Structures & Algorithms
const INITIAL_STUDENTS: StudentGradeRecord[] = [
  {
    id: 'stu-01',
    studentId: '2111001',
    fullName: 'Nguyễn Văn An',
    email: 'an.nguyen21@hcmut.edu.vn',
    avatarBg: 'from-blue-500 to-indigo-600',
    submissionsCount: 24,
    lastActive: '10 phút trước',
    scores: {
      'prob-01': 100,
      'prob-02': 100,
      'prob-03': 100,
      'prob-04': 90,
      'prob-05': 85,
      'prob-06': 100,
      'prob-07': 100,
      'prob-08': 95,
    },
    totalScore: 96.2,
    status: 'Xuất sắc',
  },
  {
    id: 'stu-02',
    studentId: '2111045',
    fullName: 'Trần Thị Mai Hương',
    email: 'huong.tran21@hcmut.edu.vn',
    avatarBg: 'from-emerald-500 to-teal-600',
    submissionsCount: 19,
    lastActive: '1 giờ trước',
    scores: {
      'prob-01': 100,
      'prob-02': 100,
      'prob-03': 95,
      'prob-04': 80,
      'prob-05': 80,
      'prob-06': 85,
      'prob-07': 90,
      'prob-08': 100,
    },
    totalScore: 91.2,
    status: 'Xuất sắc',
  },
  {
    id: 'stu-03',
    studentId: '2111089',
    fullName: 'Lê Hoàng Nam',
    email: 'nam.le21@hcmut.edu.vn',
    avatarBg: 'from-purple-500 to-violet-600',
    submissionsCount: 15,
    lastActive: 'Hôm qua',
    scores: {
      'prob-01': 100,
      'prob-02': 80,
      'prob-03': 90,
      'prob-04': 75,
      'prob-05': 70,
      'prob-06': 65,
      'prob-07': 100,
      'prob-08': 80,
    },
    totalScore: 82.5,
    status: 'Đạt',
  },
  {
    id: 'stu-04',
    studentId: '2111112',
    fullName: 'Phạm Minh Đức',
    email: 'duc.pham21@hcmut.edu.vn',
    avatarBg: 'from-amber-500 to-orange-600',
    submissionsCount: 12,
    lastActive: '3 giờ trước',
    scores: {
      'prob-01': 100,
      'prob-02': 75,
      'prob-03': 85,
      'prob-04': 60,
      'prob-05': 50,
      'prob-06': 60,
      'prob-07': 90,
      'prob-08': 70,
    },
    totalScore: 73.8,
    status: 'Đạt',
  },
  {
    id: 'stu-05',
    studentId: '2111158',
    fullName: 'Võ Quốc Bảo',
    email: 'bao.vo21@hcmut.edu.vn',
    avatarBg: 'from-rose-500 to-red-600',
    submissionsCount: 8,
    lastActive: '3 ngày trước',
    scores: {
      'prob-01': 60,
      'prob-02': 40,
      'prob-03': 50,
      'prob-04': 0,
      'prob-05': 0,
      'prob-06': 30,
      'prob-07': 0,
      'prob-08': 40,
    },
    totalScore: 27.5,
    status: 'Cần trợ giúp',
  },
  {
    id: 'stu-06',
    studentId: '2111190',
    fullName: 'Đặng Thảo Vy',
    email: 'vy.dang21@hcmut.edu.vn',
    avatarBg: 'from-pink-500 to-rose-600',
    submissionsCount: 22,
    lastActive: '30 phút trước',
    scores: {
      'prob-01': 100,
      'prob-02': 100,
      'prob-03': 100,
      'prob-04': 85,
      'prob-05': 90,
      'prob-06': 95,
      'prob-07': 100,
      'prob-08': 90,
    },
    totalScore: 95.0,
    status: 'Xuất sắc',
  },
  {
    id: 'stu-07',
    studentId: '2111224',
    fullName: 'Bùi Gia Huy',
    email: 'huy.bui21@hcmut.edu.vn',
    avatarBg: 'from-cyan-500 to-blue-600',
    submissionsCount: 14,
    lastActive: '5 giờ trước',
    scores: {
      'prob-01': 100,
      'prob-02': 70,
      'prob-03': 80,
      'prob-04': 65,
      'prob-05': 60,
      'prob-06': 70,
      'prob-07': 85,
      'prob-08': 75,
    },
    totalScore: 75.6,
    status: 'Đạt',
  },
  {
    id: 'stu-08',
    studentId: '2111280',
    fullName: 'Hoàng Kim Ngân',
    email: 'ngan.hoang21@hcmut.edu.vn',
    avatarBg: 'from-amber-400 to-yellow-600',
    submissionsCount: 7,
    lastActive: '4 ngày trước',
    scores: {
      'prob-01': 50,
      'prob-02': 30,
      'prob-03': 40,
      'prob-04': 0,
      'prob-05': 20,
      'prob-06': 0,
      'prob-07': 50,
      'prob-08': 0,
    },
    totalScore: 23.8,
    status: 'Cần trợ giúp',
  },
];

export const InstructorDashboardModal: React.FC<InstructorDashboardModalProps> = ({
  isOpen,
  onClose,
  onOpenProblemSet,
  onPublishAssignment,
}) => {
  const [activeTab, setActiveTab] = useState<'gradebook' | 'authoring' | 'analytics'>('gradebook');
  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState<'all' | 'Xuất sắc' | 'Đạt' | 'Cần trợ giúp'>('all');
  const [selectedStudent, setSelectedStudent] = useState<StudentGradeRecord | null>(null);

  // New assignment form state
  const [newTitle, setNewTitle] = useState('');
  const [newDifficulty, setNewDifficulty] = useState<'Dễ' | 'Trung bình' | 'Khó'>('Dễ');
  const [newCategory, setNewCategory] = useState<'Array' | 'String' | 'LinkedList' | 'Stack' | 'Tree' | 'DP' | 'BinarySearch' | 'SQL'>('Array');
  const [newDescription, setNewDescription] = useState('');
  const [newInputDesc, setNewInputDesc] = useState('');
  const [newOutputDesc, setNewOutputDesc] = useState('');
  const [newTestInput, setNewTestInput] = useState('');
  const [newTestOutput, setNewTestOutput] = useState('');
  const [newStarterCode, setNewStarterCode] = useState('# Viết lời giải thuật toán ở đây\nimport sys\n\ndef solution():\n    pass\n');
  const [publishedSuccess, setPublishedSuccess] = useState(false);

  // Filtered students
  const filteredStudents = useMemo(() => {
    return INITIAL_STUDENTS.filter((stu) => {
      const matchSearch =
        searchQuery.trim() === '' ||
        stu.fullName.toLowerCase().includes(searchQuery.toLowerCase()) ||
        stu.studentId.includes(searchQuery) ||
        stu.email.toLowerCase().includes(searchQuery.toLowerCase());
      const matchStatus = statusFilter === 'all' || stu.status === statusFilter;
      return matchSearch && matchStatus;
    });
  }, [searchQuery, statusFilter]);

  // Overall class analytics
  const classStats = useMemo(() => {
    const total = INITIAL_STUDENTS.length;
    const avgScore = Number((INITIAL_STUDENTS.reduce((acc, s) => acc + s.totalScore, 0) / total).toFixed(1));
    const passed = INITIAL_STUDENTS.filter((s) => s.status !== 'Cần trợ giúp').length;
    const passedRate = Math.round((passed / total) * 100);
    const needHelp = INITIAL_STUDENTS.filter((s) => s.status === 'Cần trợ giúp').length;
    return { total, avgScore, passedRate, needHelp };
  }, []);

  if (!isOpen) return null;

  // Export gradebook to CSV
  const handleExportCSV = () => {
    const headers = [
      'MSSV',
      'Họ và tên',
      'Email',
      'Bài 1 (Two Sum)',
      'Bài 2 (Parentheses)',
      'Bài 3 (Binary Search)',
      'Bài 4 (Merge Intervals)',
      'Bài 5 (LIS)',
      'Bài 6 (Islands)',
      'Bài 7 (SQL)',
      'Bài 8 (Linked List)',
      'Điểm tổng kết',
      'Trạng thái'
    ];

    const rows = INITIAL_STUDENTS.map((s) => [
      s.studentId,
      `"${s.fullName}"`,
      s.email,
      s.scores['prob-01'] ?? 0,
      s.scores['prob-02'] ?? 0,
      s.scores['prob-03'] ?? 0,
      s.scores['prob-04'] ?? 0,
      s.scores['prob-05'] ?? 0,
      s.scores['prob-06'] ?? 0,
      s.scores['prob-07'] ?? 0,
      s.scores['prob-08'] ?? 0,
      s.totalScore,
      `"${s.status}"`
    ]);

    const csvContent = 'data:text/csv;charset=utf-8,\uFEFF' + [headers.join(','), ...rows.map(e => e.join(','))].join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', `Bang_Diem_CS102_${Date.now()}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const handleCreateAssignment = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim() || !newDescription.trim()) return;

    const created: CodingProblem = {
      id: `prob-${Date.now()}`,
      number: PROBLEMS_DATA.length + 1,
      title: newTitle.trim(),
      difficulty: newDifficulty,
      category: newCategory,
      acceptanceRate: '100%',
      description: newDescription.trim(),
      inputDesc: newInputDesc.trim() || 'Dữ liệu đầu vào tiêu chuẩn stdin',
      outputDesc: newOutputDesc.trim() || 'Kết quả in ra stdout',
      constraints: ['1 <= n <= 10^5'],
      examples: [
        {
          input: newTestInput || '1 2 3',
          output: newTestOutput || '6',
          explanation: 'Ví dụ mẫu do giảng viên cấu hình.'
        }
      ],
      starterCode: {
        python: newStarterCode
      },
      testCases: [
        {
          id: 1,
          name: 'Test Case 1 (Công khai)',
          input: newTestInput || '1 2 3',
          expectedOutput: newTestOutput || '6'
        }
      ],
      hintPrompt: `Hãy hướng dẫn giải bài toán: ${newTitle} theo phương pháp gợi mở Socratic.`
    };

    if (onPublishAssignment) {
      onPublishAssignment(created);
    }

    setPublishedSuccess(true);
    setTimeout(() => {
      setPublishedSuccess(false);
      setNewTitle('');
      setNewDescription('');
      setNewInputDesc('');
      setNewOutputDesc('');
      setNewTestInput('');
      setNewTestOutput('');
    }, 2500);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/75 backdrop-blur-md animate-in fade-in duration-200">
      <div className="flex flex-col w-full max-w-6xl h-[92vh] bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl overflow-hidden animate-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 dark:border-slate-800 bg-gradient-to-r from-blue-50/70 via-white to-indigo-50/40 dark:from-slate-900 dark:via-slate-900 dark:to-indigo-950/30 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-tr from-blue-600 to-indigo-600 text-white shadow-md shadow-blue-500/25">
              <GraduationCap className="h-6 w-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-black text-slate-900 dark:text-white tracking-tight">
                  Bảng Điều Khiển Giảng Viên & Quản Lý Lớp Học
                </h2>
                <span className="rounded-full bg-blue-100 dark:bg-blue-900/60 px-2.5 py-0.5 text-[10px] font-extrabold text-blue-700 dark:text-blue-300">
                  Lớp CS102: Cấu Trúc Dữ Liệu & Giải Thuật
                </span>
              </div>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Theo dõi tiến độ chấm điểm tự động, tỷ lệ vượt qua bài tập và xuất bản bài thi LeetCode mới
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

        {/* Navigation Tabs & Overview Metrics Bar */}
        <div className="px-6 py-3 border-b border-slate-200/80 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-950/40 flex flex-wrap items-center justify-between gap-4 shrink-0">
          {/* Tabs */}
          <div className="flex items-center gap-1.5 bg-slate-200/70 dark:bg-slate-800 p-1 rounded-2xl">
            <button
              type="button"
              onClick={() => setActiveTab('gradebook')}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs font-extrabold transition ${
                activeTab === 'gradebook'
                  ? 'bg-white dark:bg-slate-700 text-blue-600 dark:text-blue-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <FileSpreadsheet className="h-3.5 w-3.5" />
              <span>Ma Trận Bảng Điểm ({INITIAL_STUDENTS.length} SV)</span>
            </button>

            <button
              type="button"
              onClick={() => setActiveTab('authoring')}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs font-extrabold transition ${
                activeTab === 'authoring'
                  ? 'bg-white dark:bg-slate-700 text-blue-600 dark:text-blue-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <Plus className="h-3.5 w-3.5" />
              <span>Tạo Bài Tập / Đề Thi Mới</span>
            </button>
          </div>

          {/* Quick Metrics */}
          <div className="flex items-center gap-4 text-xs font-bold text-slate-600 dark:text-slate-300">
            <div className="flex items-center gap-1.5">
              <span className="text-slate-400">Điểm TB Lớp:</span>
              <span className="text-blue-600 dark:text-blue-400 font-extrabold">{classStats.avgScore} / 100</span>
            </div>
            <div className="flex items-center gap-1.5">
              <span className="text-slate-400">Tỷ Lệ Đạt:</span>
              <span className="text-emerald-600 dark:text-emerald-400 font-extrabold">{classStats.passedRate}%</span>
            </div>
            {classStats.needHelp > 0 && (
              <div className="flex items-center gap-1.5 text-rose-500">
                <AlertCircle className="h-3.5 w-3.5" />
                <span>{classStats.needHelp} SV cần hỗ trợ</span>
              </div>
            )}
          </div>
        </div>

        {/* Tab 1: Gradebook Matrix */}
        {activeTab === 'gradebook' && (
          <div className="flex-1 flex flex-col overflow-hidden p-6 space-y-4">
            {/* Filter and Export Bar */}
            <div className="flex flex-wrap items-center justify-between gap-3 shrink-0">
              <div className="flex items-center gap-2 flex-1 min-w-[240px] max-w-md bg-slate-50 dark:bg-slate-800 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700">
                <Search className="h-4 w-4 text-slate-400" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Tìm kiếm sinh viên theo tên hoặc MSSV..."
                  className="w-full bg-transparent text-xs text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none font-medium"
                />
              </div>

              <div className="flex items-center gap-2">
                {/* Status filter pills */}
                <div className="flex items-center rounded-xl bg-slate-100 dark:bg-slate-800 p-0.5 text-xs font-bold text-slate-600 dark:text-slate-400">
                  {['all', 'Xuất sắc', 'Đạt', 'Cần trợ giúp'].map((st) => (
                    <button
                      key={st}
                      type="button"
                      onClick={() => setStatusFilter(st as any)}
                      className={`px-3 py-1 rounded-lg transition ${
                        statusFilter === st
                          ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs'
                          : 'hover:text-slate-900 dark:hover:text-white'
                      }`}
                    >
                      {st === 'all' ? 'Tất cả trạng thái' : st}
                    </button>
                  ))}
                </div>

                {/* Export button */}
                <button
                  type="button"
                  onClick={handleExportCSV}
                  className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition shadow-md shadow-emerald-500/20 active:scale-[0.98]"
                >
                  <Download className="h-3.5 w-3.5" />
                  <span>Xuất Bảng Điểm (.CSV)</span>
                </button>
              </div>
            </div>

            {/* Table Container */}
            <div className="flex-1 overflow-x-auto rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm">
              <table className="w-full text-left text-xs border-collapse">
                <thead className="bg-slate-50/80 dark:bg-slate-950/60 border-b border-slate-200 dark:border-slate-800 text-[11px] font-black uppercase tracking-wider text-slate-500 dark:text-slate-400 sticky top-0 z-10 backdrop-blur-sm">
                  <tr>
                    <th className="py-3 px-4">Sinh Viên</th>
                    <th className="py-3 px-3">MSSV</th>
                    <th className="py-3 px-2 text-center" title="Two Sum">#1</th>
                    <th className="py-3 px-2 text-center" title="Valid Parentheses">#2</th>
                    <th className="py-3 px-2 text-center" title="Binary Search">#3</th>
                    <th className="py-3 px-2 text-center" title="Merge Intervals">#4</th>
                    <th className="py-3 px-2 text-center" title="LIS">#5</th>
                    <th className="py-3 px-2 text-center" title="Islands">#6</th>
                    <th className="py-3 px-2 text-center" title="SQL">#7</th>
                    <th className="py-3 px-2 text-center" title="Reverse List">#8</th>
                    <th className="py-3 px-4 text-center">Điểm TB</th>
                    <th className="py-3 px-4 text-center">Trạng Thái</th>
                    <th className="py-3 px-3 text-right">Chi Tiết</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 dark:divide-slate-800/60 font-medium">
                  {filteredStudents.map((stu) => (
                    <tr
                      key={stu.id}
                      className="hover:bg-slate-50/60 dark:hover:bg-slate-800/40 transition cursor-pointer"
                      onClick={() => setSelectedStudent(stu)}
                    >
                      {/* Name & Avatar */}
                      <td className="py-3 px-4">
                        <div className="flex items-center gap-2.5">
                          <div className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-gradient-to-tr ${stu.avatarBg} text-white font-black text-xs shadow-xs`}>
                            {stu.fullName.split(' ').slice(-1)[0][0]}
                          </div>
                          <div>
                            <div className="font-extrabold text-slate-900 dark:text-slate-100">
                              {stu.fullName}
                            </div>
                            <div className="text-[11px] text-slate-400">
                              {stu.email}
                            </div>
                          </div>
                        </div>
                      </td>

                      {/* Student ID */}
                      <td className="py-3 px-3 font-mono text-slate-500 dark:text-slate-400">
                        {stu.studentId}
                      </td>

                      {/* Scores for Problems #1 to #8 */}
                      {['prob-01', 'prob-02', 'prob-03', 'prob-04', 'prob-05', 'prob-06', 'prob-07', 'prob-08'].map((pid) => {
                        const sc = stu.scores[pid] ?? 0;
                        return (
                          <td key={pid} className="py-3 px-2 text-center font-mono">
                            <span className={`inline-block px-1.5 py-0.5 rounded text-[11px] font-bold ${
                              sc >= 90
                                ? 'bg-emerald-100 dark:bg-emerald-950/80 text-emerald-700 dark:text-emerald-300'
                                : sc >= 60
                                ? 'bg-amber-100 dark:bg-amber-950/80 text-amber-700 dark:text-amber-300'
                                : sc > 0
                                ? 'bg-orange-100 dark:bg-orange-950/80 text-orange-700 dark:text-orange-300'
                                : 'bg-slate-100 dark:bg-slate-800 text-slate-400'
                            }`}>
                              {sc}
                            </span>
                          </td>
                        );
                      })}

                      {/* Total Score */}
                      <td className="py-3 px-4 text-center font-black text-sm">
                        <span className={stu.totalScore >= 80 ? 'text-blue-600 dark:text-blue-400' : stu.totalScore >= 50 ? 'text-amber-600 dark:text-amber-400' : 'text-rose-500'}>
                          {stu.totalScore}
                        </span>
                      </td>

                      {/* Status */}
                      <td className="py-3 px-4 text-center">
                        <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-extrabold ${
                          stu.status === 'Xuất sắc'
                            ? 'bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800'
                            : stu.status === 'Đạt'
                            ? 'bg-blue-50 dark:bg-blue-950/60 text-blue-600 dark:text-blue-400 border border-blue-300 dark:border-blue-800'
                            : 'bg-rose-50 dark:bg-rose-950/60 text-rose-600 dark:text-rose-400 border border-rose-300 dark:border-rose-800'
                        }`}>
                          {stu.status}
                        </span>
                      </td>

                      {/* Detail action */}
                      <td className="py-3 px-3 text-right">
                        <button
                          type="button"
                          className="p-1.5 rounded-lg text-slate-400 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                          title="Xem chi tiết sinh viên"
                        >
                          <ChevronRight className="h-4 w-4" />
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Student Detail Modal Drawer */}
            {selectedStudent && (
              <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs">
                <div className="w-full max-w-lg bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-6 shadow-2xl space-y-4 animate-in zoom-in-95">
                  <div className="flex items-center justify-between pb-3 border-b border-slate-200 dark:border-slate-800">
                    <div className="flex items-center gap-3">
                      <div className={`flex h-10 w-10 items-center justify-center rounded-2xl bg-gradient-to-tr ${selectedStudent.avatarBg} text-white font-black text-sm`}>
                        {selectedStudent.fullName.split(' ').slice(-1)[0][0]}
                      </div>
                      <div>
                        <h3 className="font-extrabold text-slate-900 dark:text-white">
                          {selectedStudent.fullName}
                        </h3>
                        <p className="text-xs text-slate-400 font-mono">
                          MSSV: {selectedStudent.studentId} • {selectedStudent.email}
                        </p>
                      </div>
                    </div>
                    <button
                      type="button"
                      onClick={() => setSelectedStudent(null)}
                      className="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
                    >
                      <X className="h-5 w-5" />
                    </button>
                  </div>

                  <div className="grid grid-cols-3 gap-3 text-center">
                    <div className="p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800">
                      <div className="text-xs text-slate-400 mb-0.5">Điểm TB</div>
                      <div className="text-lg font-black text-blue-600 dark:text-blue-400">{selectedStudent.totalScore}</div>
                    </div>
                    <div className="p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800">
                      <div className="text-xs text-slate-400 mb-0.5">Số lần nộp</div>
                      <div className="text-lg font-black text-slate-800 dark:text-slate-200">{selectedStudent.submissionsCount}</div>
                    </div>
                    <div className="p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800">
                      <div className="text-xs text-slate-400 mb-0.5">Hoạt động</div>
                      <div className="text-xs font-bold text-slate-700 dark:text-slate-300 mt-1">{selectedStudent.lastActive}</div>
                    </div>
                  </div>

                  <div>
                    <h4 className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">
                      Chi tiết điểm từng bài toán LeetCode
                    </h4>
                    <div className="grid grid-cols-2 gap-2 text-xs">
                      {['prob-01', 'prob-02', 'prob-03', 'prob-04', 'prob-05', 'prob-06', 'prob-07', 'prob-08'].map((pid, idx) => {
                        const sc = selectedStudent.scores[pid] ?? 0;
                        return (
                          <div key={pid} className="flex items-center justify-between p-2 rounded-xl bg-slate-50 dark:bg-slate-800/40 border border-slate-100 dark:border-slate-800">
                            <span className="text-slate-600 dark:text-slate-300">Bài #{idx + 1}</span>
                            <span className={`font-mono font-bold ${sc >= 80 ? 'text-emerald-500' : sc >= 50 ? 'text-amber-500' : 'text-rose-500'}`}>
                              {sc} / 100
                            </span>
                          </div>
                        );
                      })}
                    </div>
                  </div>

                  <div className="pt-2 flex justify-end">
                    <button
                      type="button"
                      onClick={() => setSelectedStudent(null)}
                      className="px-4 py-2 rounded-xl bg-blue-600 text-white text-xs font-bold hover:bg-blue-700 transition"
                    >
                      Đóng
                    </button>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}

        {/* Tab 2: Assignment Authoring */}
        {activeTab === 'authoring' && (
          <div className="flex-1 overflow-y-auto p-6 space-y-6">
            <div className="max-w-3xl mx-auto space-y-4">
              <div>
                <h3 className="text-lg font-black text-slate-900 dark:text-white">
                  Soạn Thảo Bài Tập / Đề Thi Thuật Toán Mới
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                  Cấu hình đề bài, ngôn ngữ hỗ trợ và bộ dữ liệu test case tự động chấm điểm cho học viên
                </p>
              </div>

              {publishedSuccess && (
                <div className="p-4 rounded-2xl bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-300 dark:border-emerald-700 text-emerald-800 dark:text-emerald-300 flex items-center gap-3 animate-in fade-in">
                  <CheckCircle2 className="h-5 w-5 text-emerald-500 shrink-0" />
                  <div className="text-xs font-bold">
                    Xuất bản bài tập thành công! Đã bổ sung vào Kho Bài Tập LeetCode & Đấu Trường.
                  </div>
                </div>
              )}

              <form onSubmit={handleCreateAssignment} className="space-y-4 text-xs">
                {/* Title & Metadata */}
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div className="sm:col-span-2">
                    <label className="block text-slate-700 dark:text-slate-300 font-bold mb-1">
                      Tiêu đề bài toán:
                    </label>
                    <input
                      type="text"
                      required
                      value={newTitle}
                      onChange={(e) => setNewTitle(e.target.value)}
                      placeholder="Ví dụ: Tìm Chuỗi Đối Xứng Palindrome Dài Nhất"
                      className="w-full rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 px-3.5 py-2.5 text-xs text-slate-900 dark:text-slate-100 focus:outline-none focus:border-blue-500 font-medium"
                    />
                  </div>

                  <div>
                    <label className="block text-slate-700 dark:text-slate-300 font-bold mb-1">
                      Độ khó:
                    </label>
                    <select
                      value={newDifficulty}
                      onChange={(e) => setNewDifficulty(e.target.value as any)}
                      className="w-full rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 px-3 py-2.5 text-xs text-slate-900 dark:text-slate-100 focus:outline-none focus:border-blue-500 font-bold"
                    >
                      <option value="Dễ">Dễ (Easy)</option>
                      <option value="Trung bình">Trung bình (Medium)</option>
                      <option value="Khó">Khó (Hard)</option>
                    </select>
                  </div>
                </div>

                {/* Category */}
                <div>
                  <label className="block text-slate-700 dark:text-slate-300 font-bold mb-1">
                    Chủ đề giải thuật:
                  </label>
                  <select
                    value={newCategory}
                    onChange={(e) => setNewCategory(e.target.value as any)}
                    className="w-full rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 px-3.5 py-2 text-xs text-slate-900 dark:text-slate-100 focus:outline-none focus:border-blue-500 font-medium"
                  >
                    <option value="Array">Mảng & Hash Map (Array)</option>
                    <option value="String">Xử lý Chuỗi (String)</option>
                    <option value="Stack">Ngăn xếp & Hàng đợi (Stack / Queue)</option>
                    <option value="LinkedList">Danh sách liên kết (LinkedList)</option>
                    <option value="BinarySearch">Tìm kiếm nhị phân (Binary Search)</option>
                    <option value="DP">Quy hoạch động (Dynamic Programming)</option>
                    <option value="Tree">Cây & Đồ thị (Tree / Graph)</option>
                    <option value="SQL">Truy vấn cơ sở dữ liệu (SQL)</option>
                  </select>
                </div>

                {/* Description */}
                <div>
                  <label className="block text-slate-700 dark:text-slate-300 font-bold mb-1">
                    Mô tả đề bài chi tiết (Markdown hỗ trợ):
                  </label>
                  <textarea
                    rows={4}
                    required
                    value={newDescription}
                    onChange={(e) => setNewDescription(e.target.value)}
                    placeholder="Mô tả yêu cầu bài toán, các điều kiện đầu vào và đầu ra..."
                    className="w-full rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 p-3 text-xs text-slate-900 dark:text-slate-100 focus:outline-none focus:border-blue-500 font-medium leading-relaxed"
                  />
                </div>

                {/* Input / Output Desc */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label className="block text-slate-700 dark:text-slate-300 font-bold mb-1">
                      Quy cách đầu vào (Input Format):
                    </label>
                    <input
                      type="text"
                      value={newInputDesc}
                      onChange={(e) => setNewInputDesc(e.target.value)}
                      placeholder="Dòng 1 chứa số nguyên N..."
                      className="w-full rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 px-3 py-2 text-xs text-slate-900 dark:text-slate-100 focus:outline-none focus:border-blue-500"
                    />
                  </div>

                  <div>
                    <label className="block text-slate-700 dark:text-slate-300 font-bold mb-1">
                      Quy cách đầu ra (Output Format):
                    </label>
                    <input
                      type="text"
                      value={newOutputDesc}
                      onChange={(e) => setNewOutputDesc(e.target.value)}
                      placeholder="In ra giá trị tìm được trên 1 dòng..."
                      className="w-full rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 px-3 py-2 text-xs text-slate-900 dark:text-slate-100 focus:outline-none focus:border-blue-500"
                    />
                  </div>
                </div>

                {/* Test case pair */}
                <div className="p-4 rounded-2xl bg-blue-50/40 dark:bg-blue-950/20 border border-blue-200 dark:border-blue-900/50 space-y-2">
                  <div className="font-bold text-blue-700 dark:text-blue-300 text-xs">
                    Bộ Test Case mẫu công khai:
                  </div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 font-mono">
                    <div>
                      <span className="text-[11px] text-slate-400 block mb-1">Input mẫu:</span>
                      <textarea
                        rows={2}
                        value={newTestInput}
                        onChange={(e) => setNewTestInput(e.target.value)}
                        placeholder="1 2 3"
                        className="w-full rounded-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 p-2 text-xs text-slate-900 dark:text-slate-100 focus:outline-none"
                      />
                    </div>
                    <div>
                      <span className="text-[11px] text-slate-400 block mb-1">Expected Output mẫu:</span>
                      <textarea
                        rows={2}
                        value={newTestOutput}
                        onChange={(e) => setNewTestOutput(e.target.value)}
                        placeholder="6"
                        className="w-full rounded-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 p-2 text-xs text-slate-900 dark:text-slate-100 focus:outline-none text-emerald-500"
                      />
                    </div>
                  </div>
                </div>

                <div className="pt-2 flex justify-end gap-3">
                  <button
                    type="button"
                    onClick={() => setActiveTab('gradebook')}
                    className="px-4 py-2 rounded-xl text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 font-bold transition"
                  >
                    Hủy bỏ
                  </button>
                  <button
                    type="submit"
                    className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-extrabold shadow-md shadow-blue-500/25 transition active:scale-[0.98]"
                  >
                    <Send className="h-4 w-4" />
                    <span>Xuất Bản Bài Tập Ngay</span>
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

      </div>
    </div>
  );
};
