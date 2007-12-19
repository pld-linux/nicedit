Summary:	Micro Inline WYSIWY
Name:		nicedit
Version:	0.26
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://nicedit.com/nicEdit-full.zip
# Source0-md5:	360663edaa06259ea1cbdd8f4066cbc5
URL:		http://nicedit.com/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
NicEdit is a Javascript/AJAX inline content editor to allow easy
editing of web site content on the fly in the browser. It integrates
into any site in seconds to make any element/div editable or convert
standard textareas to rich text editing.

%prep
%setup -q -n nicEditor

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a nicEdit.js nicEditorIcons.gif $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_appdir}
