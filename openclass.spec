Summary:	Simple open-source solution for class control
Name:		openclass
Version:	0.4
Release:	3
Source0:	%name-%version.tar.bz2
License:	GPLv2
Group:		Networking/Other
Url:		https://github.com/eugeni/openclass
BuildRequires: python-devel
BuildArch: noarch
Requires:  python
Requires:  pygtk2.0
Requires:  python-notify

%description
OpenClass is a simple open-source solution for class control, designed with the
following features in mind:
- small footprint
- light-weight functionality
- minimum of non-essential features

If you already know how italc, bluelab, mythware, iClass and similar solutions
work, you already know what OpenClass is.

%prep
%setup -q

%build

%install
%makeinstall_std
%find_lang %name


%clean

%files -f %{name}.lang
%doc README
%_bindir/openclass-student
%_bindir/openclass-teacher
%_datadir/openclass/
%_datadir/applications/openclass-student.desktop
%_datadir/applications/openclass-teacher.desktop


%changelog
* Mon Jun 27 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.4-1mdv2011.0
+ Revision: 687600
- New version 0.4.

* Thu Jun 02 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.3-1
+ Revision: 682418
- New version 0.3

* Mon May 30 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.2-1
+ Revision: 681968
- Updated to 0.2

* Sat May 28 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.1-1
+ Revision: 680789
- Imported to cooker upon requests.
- Created package structure for openclass.

