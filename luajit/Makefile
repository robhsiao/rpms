all: build dist

download:
	spectool -g -R luv-t*.spec

rebuild: download
	rpmbuild --short-circuit -bi luv-luajit.spec

build: download
	rpmbuild -bb luv-luajit.spec

dist:
	find ~/rpmbuild/RPMS -name "*.rpm" | xargs -I{} mv "{}" .

clean:
	rm ~/.rpmmacros
	rm -rf ~/rpmbuild
	rpmdev-setuptree
