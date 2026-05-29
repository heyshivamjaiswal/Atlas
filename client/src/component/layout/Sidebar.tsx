import {
  Archive,
  FileText,
  Globe,
  LayoutGrid,
  Settings,
  Star,
  Video,
} from 'lucide-react';
import Link from 'next/link';

export default function Sidebar() {
  return (
    <aside className="w-64 bg-sidebar border-r border-border flex flex-col min-h-screen">
      {/* Header */}
      <div className="p-6 border-b border-border">
        <div className="flex items-center gap-3">
          <div className="h-8 w-8 rounded-md bg-white text-black flex items-center justify-center font-semibold">
            A
          </div>
          <span className="font-semibold text-lg">Atlas</span>
        </div>
      </div>

      {/* content */}
      <div className="flex-1 p-4">
        {/* library */}

        <div>
          <p className="text-xs uppercase text-muted mb-4">Library</p>

          <div className="space-y-1">
            <SidebarItem
              href="/dashboard"
              icon={<LayoutGrid size={18} />}
              label="All sources"
            />

            <SidebarItem
              href="/dashboard/pdfs"
              icon={<FileText size={18} />}
              label="PDFs"
            />

            <SidebarItem
              href="/dashboard/web"
              icon={<Globe size={18} />}
              label="Websites"
            />

            <SidebarItem
              href="/dashboard/videos"
              icon={<Video size={18} />}
              label="videos"
            />
          </div>
        </div>

        {/* Workspace */}
        <div className="mt-10">
          <p className="text-xs uppercase text-muted mb-4">Workspace</p>
          <SidebarItem
            href="/dashboard/starred"
            icon={<Star size={18} />}
            label="Starred"
          />

          <SidebarItem
            href="/dashboard/archive"
            icon={<Archive size={18} />}
            label="Archive"
          />

          <SidebarItem
            href="/dashboard/settings"
            icon={<Settings size={18} />}
            label="settings"
          />
        </div>
      </div>

      {/* Footer */}
      <div className="border-t border-border p-4">
        <div className="flex items-center gap-3">
          <div className="h-10 w-10 rounded-full bg-card flex items-center justify-center">
            SJ
          </div>
          <div>
            <p className="text-sm font-medium">Shivam Jaiswal</p>
            <p className="text-xs text-muted">Personal workspace</p>
          </div>
        </div>
      </div>
    </aside>
  );
}

type SidebarItemProps = {
  icon: React.ReactNode;
  label: string;
  href: string;
};

function SidebarItem({ icon, label, href }: SidebarItemProps) {
  return (
    <Link
      href={href}
      className="flex items-center gap-3 rounded-md px-3 py-2 hover:bg-card transition-colors"
    >
      {icon}
      <span>{label}</span>
    </Link>
  );
}
