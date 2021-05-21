{
  pkgs ? import <nixpkgs> {},
  delveBinary ? "",
  doCheck ? true
}:

let

app = pkgs.poetry2nix.mkPoetryApplication {
  projectDir = ./client;
  pyproject = ./client/pyproject.toml;
  poetrylock = ./client/poetry.lock;
  src = ./client;
};

in

app.overrideAttrs(oldAttrs: rec {
  name = "delve-client-${version}";
  version = "1.1.3";
  nativeBuildInputs = oldAttrs.nativeBuildInputs ++ [ delveBinary ];
  checkPhase = ''
    mkdir home
    export HOME=$PWD/home

    delve server &
    PID=$!
    sleep 15s

    pytest integration_tests || (kill -9 $PID && exit 1)
    echo "Shutting down delve server. Pid: $PID"
    kill -9 $PID
  '';
  doCheck = doCheck;
})

