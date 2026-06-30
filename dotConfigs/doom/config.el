;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!


;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets. It is optional.
;; (setq user-full-name "John Doe"
;;       user-mail-address "john@doe.com")

;; Doom exposes five (optional) variables for controlling fonts in Doom:
;;
;; - `doom-font' -- the primary font to use
;; - `doom-variable-pitch-font' -- a non-monospace font (where applicable)
;; - `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;; - `doom-symbol-font' -- for symbols
;; - `doom-serif-font' -- for the `fixed-pitch-serif' face
;;
;; See 'C-h v doom-font' for documentation and more examples of what they
;; accept. For example:
;;
;;(setq doom-font (font-spec :family "Fira Code" :size 12 :weight 'semi-light)
;;      doom-variable-pitch-font (font-spec :family "Fira Sans" :size 13))
;;
;; If you or Emacs can't find your font, use 'M-x describe-font' to look them

;; up, `M-x eval-region' to execute elisp code, and 'M-x doom/reload-font' to
;; refresh your font settings. If Emacs still can't find your font, it likely
;; wasn't installed correctly. Font issues are rarely Doom issues!

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-solarized-dark)
(setq doom-font (font-spec :family "JetBrains Mono" :size 14 :weight 'regular))

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type t)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/org/")


;; Whenever you reconfigure a package, make sure to wrap your config in an
;; `with-eval-after-load' block, otherwise Doom's defaults may override your
;; settings. E.g.
;;
;;   (with-eval-after-load 'PACKAGE
;;     (setq x y))
;;
;; The exceptions to this rule:
;;
;;   - Setting file/directory variables (like `org-directory')
;;   - Setting variables which explicitly tell you to set them before their
;;     package is loaded (see 'C-h v VARIABLE' to look them up).
;;   - Setting doom variables (which start with 'doom-' or '+').
;;
;; Here are some additional functions/macros that will help you configure Doom.
;;
;; - `load!' for loading external *.el files relative to this one
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;; Alternatively, use `C-h o' to look up a symbol (functions, variables, faces,
;; etc).
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.



;; ---------------------------------------------------------------------------
;; AI GENERATED CONFIGS
;; ---------------------------------------------------------------------------



;; ---------------------------------------------------------------------------
;; 1. Persist buffers/workspaces across restarts (per-project, automatically)
;; ---------------------------------------------------------------------------
;; Doom's `workspaces` module already saves/restores via `persp-mode'.
;; This makes it auto-save on exit and auto-load the last session on startup,
;; so reopening a project (via `SPC p p`) restores the buffers you had open.
(setq persp-auto-save-opt 1          ; auto-save when you exit
      persp-auto-resume-time 0.1)    ; auto-restore last session on startup

;; If you'd rather restore sessions manually instead of automatically, comment
;; out the line above and use `SPC q s` / `SPC q l` (doom/save-session,
;; doom/load-session) or `SPC w l` for project-specific workspace loading.


;; ---------------------------------------------------------------------------
;; 2. Smaller font in Treemacs so deeply nested filenames are readable
;; ---------------------------------------------------------------------------
;; (Doom already provides a face for this: `treemacs-window-background-face')
(after! treemacs
  (add-hook 'treemacs-mode-hook
            (lambda ()
              (face-remap-add-relative 'default :height 0.7))))
;; Adjust 0.8 to taste (1.0 = same as everywhere else, lower = smaller).

;; ---------------------------------------------------------------------------
;; 3. Spring Boot / Java navigation (go to implementation, find usages)
;; ---------------------------------------------------------------------------
;; You already have `(java +lsp)', so lsp-java provides this via xref.
;; Doom's defaults already bind these, but listed here for clarity:
;;   gd          -> lsp-find-definition / xref-find-definitions
;;   gD          -> lsp-find-declaration
;;   gI          -> lsp-find-implementation   (interface -> impl, very useful)
;;   SPC c d     -> lsp-find-declaration
;;   SPC c i     -> lsp-find-implementation
;;   SPC c R     -> lsp-rename
;; "Find usages" / references:
;;   SPC c u     -> lsp-find-references  (Doom default under :tools lookup)
;;   gr          -> lsp-find-references (evil binding, also default — may
;;                  conflict with `+eval/region' depending on mode/version)
;; NOTE: SPC c u is NOT bound by default in this Doom version — added below.
(map! :map lsp-mode-map
      :n "SPC c i" #'lsp-find-implementation
      :n "SPC c u" #'lsp-find-references)

;; ---------------------------------------------------------------------------
;; 4. Run the Spring Boot app with Gradle from inside Emacs
;; ---------------------------------------------------------------------------
;; Opens a vterm in the project root and runs `./gradlew bootRun`.
;; Bound to `SPC m r` (mnemonic: major-mode -> run) while in a Java buffer.
(set-popup-rule! "^\\*bootRun:" :side 'bottom :size 0.35 :select t :quit nil)
(defun my/spring-boot-run ()
  "Run `./gradlew bootRun` for the current project in a dedicated vterm."
  (interactive)
  (let* ((default-directory (or (doom-project-root) default-directory))
         (buf-name (format "*bootRun:%s*" (doom-project-name))))
    (if (get-buffer buf-name)
        (pop-to-buffer buf-name)
      (progn
        (vterm buf-name)
        (vterm-send-string "./gradlew bootRun")
        (vterm-send-return)))))

(map! :map java-mode-map
      :localleader
      "r" #'my/spring-boot-run)

(map! :map kotlin-mode-map
      :localleader
      "r" #'my/spring-boot-run)
;; Usage: open any .java or .kt file in your Spring Boot project, then `SPC m r'.
