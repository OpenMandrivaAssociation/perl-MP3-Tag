%define upstream_name	 MP3-Tag
%define upstream_version 1.13

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Normalize::Text::Normalize_Fields\\)|perl\\(Music_Normalize_Fields\\)'
%else
%define _requires_exceptions perl(\\(Normalize::Text::Normalize_Fields\\|Music_Normalize_Fields\\))
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Module for reading tags of MP3 audio files 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MP3/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildArch:	noarch

Requires:	perl(Compress::Zlib)

%description
Tag is a wrapper module to read different tags of mp3 files. It provides an
easy way to access the functions of separate modules which do the handling
of reading/writing the tags itself.

At the moment MP3::Tag::ID3v1 and MP3::Tag::ID3v2 are supported for read and
write; MP3::Tag::Inf, MP3::Tag::CDDB_File, MP3::Tag::File,
MP3::Tag::LastResort are supported for read access (the information obtained
by parsing CDDB files, .inf file and the filename).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# requires CDDB connection
rm -f t/mp3tag.t
chmod -R u+w examples
chmod 755 examples/*.pl examples/mp3info2 examples/typeset_audio_dir

%build
# -n is here to avoid installation of scripts (they come in examples/ anyway)
perl Makefile.PL INSTALLDIRS=vendor -n
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README.txt TODO examples
%{perl_vendorlib}/MP3
%{perl_vendorlib}/Encode
%{perl_vendorlib}/Normalize
%{_mandir}/*/*

%changelog
* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.130.0-1mdv2011.0
+ Revision: 553132
- update to 1.13

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2010.1
+ Revision: 471054
- update to 1.12

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 410092
- rebuild using %%perl_convert_version

* Sun May 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2010.0
+ Revision: 376724
- update to new version 1.11

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2010.0
+ Revision: 373734
- update to new version 1.10

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-2mdv2010.0
+ Revision: 373067
- fix deps

* Wed May 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2010.0
+ Revision: 372559
- fix dependencies
- new version

* Tue Jan 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9714-1mdv2009.1
+ Revision: 325360
- update to new version 0.9714

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.9713-1mdv2009.1
+ Revision: 299401
- update to new version 0.9713

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.9710-4mdv2009.0
+ Revision: 257932
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9710-3mdv2009.0
+ Revision: 245986
- rebuild

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 0.9710-1mdv2008.1
+ Revision: 161378
- update to new version 0.9710

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.9709-1mdv2008.0
+ Revision: 20305
- 0.9709


* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.9708-1mdv2007.0
- New version 0.9708

* Thu Jun 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.9707-1mdv2007.0
- New release 0.9707
- spec cleanup
- better sources URL

* Fri Mar 03 2006 Austin Acton <austin@mandriva.org> 0.9706-1mdk
- New release 0.9706

* Fri Feb 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.9705-1mdk
- New release 0.9705

* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.9704-1mdk
- New release 0.9704

* Mon Nov 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.9702-1mdk
- 0.9702
- fix perms, don't install scripts in _bindir

* Wed Sep 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.9701-2mdk
- fix perms

* Wed Sep 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.9701-1mdk
- new version  
- rpmbuildupdate aware
- better summary
- spec cleanup
- fix directory ownership

* Mon Jul 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.97-1mdk
- 0.97

* Thu Oct 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.94-1mdk
- 0.94
- add handy examples scripts in documentation

* Tue Jul 20 2004 Austin Acton <austin@mandrake.org> 0.92-1mdk
- 0.92

