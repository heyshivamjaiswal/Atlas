import Sidebar from '@/component/layout/Sidebar';
import Topbar from '@/component/layout/Topbar';

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex min-h-screen">
      <Sidebar />

      <main className="flex-1 bg-background">
        <Topbar />
        {children}
      </main>
    </div>
  );
}
