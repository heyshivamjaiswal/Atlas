import Topbar from '@/component/layout/Topbar';
import Sidebar from '@/component/layout/Sidebar';

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-background text-foreground">
        <div className="flex min-h-screen">
          <Sidebar />

          <main className="flex-1 bg-background">
            <Topbar />
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
